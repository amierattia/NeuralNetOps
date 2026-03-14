from openai import OpenAI
from netmiko import ConnectHandler

# ----------------------------
# Groq API
# ----------------------------

client = OpenAI(
    api_key="YourApiKey",
    base_url="https://api.groq.com/openai/v1",
)

# ----------------------------
# Cisco Device
# ----------------------------

router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.159.139",
    "username": "amier",
    "password": "123",
    "secret": "123",
}

# ----------------------------
# Detect OS
# ----------------------------

connection = ConnectHandler(**router)
connection.enable()

version_output = connection.send_command("show version")

if "IOS XE" in version_output:
    device_os = "Cisco IOS-XE"
elif "NX-OS" in version_output:
    device_os = "Cisco NX-OS"
elif "IOS" in version_output:
    device_os = "Cisco IOS"
else:
    device_os = "Cisco device"

print("Detected OS:", device_os)

connection.disconnect()

# ----------------------------
# Dangerous Commands
# ----------------------------

dangerous_commands = [
    "reload",
    "erase",
    "write erase",
    "delete",
    "format",
]

# ----------------------------
# CLI Loop
# ----------------------------

while True:

    prompt = input("AutoNet> ")

    if prompt.lower() in ["exit", "quit"]:
        break

    # ----------------------------
    # AI Command Generation
    # ----------------------------

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=[
            {
                "role": "system",
                "content": f"""You are a network automation engine.

The target device runs: {device_os}

Generate ONLY valid CLI commands for this OS.

Return ONLY commands.
No explanation.
No markdown.
No comments."""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    commands_text = response.output_text.strip()

    print("\nGenerated Commands:\n")
    print(commands_text)

    commands = commands_text.split("\n")
    commands = [cmd.strip() for cmd in commands if cmd.strip()]

    # ----------------------------
    # Safety Filter
    # ----------------------------

    for cmd in commands:
        for bad in dangerous_commands:
            if bad in cmd.lower():
                print("\nDangerous command detected:", cmd)
                print("Execution stopped.")
                exit()

    # ----------------------------
    # Confirm
    # ----------------------------

    confirm = input("\nExecute on router? (yes/no): ")

    if confirm.lower() != "yes":
        continue

    # ----------------------------
    # Execute
    # ----------------------------

    try:

        connection = ConnectHandler(**router)
        connection.enable()

        output = connection.send_config_set(commands)

        print("\nDevice Output:\n")
        print(output)

        connection.disconnect()

    except Exception as e:

        print("\nConnection Error:", e)
