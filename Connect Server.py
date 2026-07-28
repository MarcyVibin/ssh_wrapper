from pathlib import Path
import subprocess
import os

from InquirerPy import inquirer
from InquirerPy.separator import Separator

def clear():
    """Clears the terminal independent from operating system.
    """
    print("\033c", end="")


def get_ssh_hosts(config_path=Path.home() / ".ssh" / "config"):
    hosts = []

    if not config_path.exists():
        return hosts

    with config_path.open() as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if line.lower().startswith("host "):
                for host in line.split()[1:]:
                    # Skip wildcard hosts
                    if "*" in host or "?" in host or "!" in host:
                        continue

                    hosts.append(host)

    return sorted(set(hosts))

def choose_host(hosts):

    choices = (
        hosts
        + [
            Separator(),
            {"name": "Manual host...", "value": "__manual__"},
        ]
    )

    selection = inquirer.select(
        message="SSH to:",
        choices=choices,
    ).execute()

    if selection == "__manual__":
        return inquirer.text(
            message="Enter SSH target:",
        ).execute(), True

    return selection, False

def add_manual_host_to_config(target, config_name, config_path=Path.home() / ".ssh" / "config"):
    if "@" in target:
        user, hostname = target.rsplit("@", 1)
    else:
        user = None
        hostname = target

    existing_hosts = get_ssh_hosts(config_path)

    if config_name in existing_hosts:
        print(f"\nError: '{config_name}' already exists in SSH config.")
        return False

    config_path.parent.mkdir(parents=True, exist_ok=True)

    with config_path.open("a") as f:
        if config_path.stat().st_size > 0:
            f.write("\n")

        f.write(f"Host {config_name}\n")
        f.write(f"    HostName {hostname}\n")

        if user:
            f.write(f"    User {user}\n")

    print(f"\nAdded '{config_name}' to SSH config.")
    return True

def ask_to_save_manual_host(target):
    save = inquirer.confirm(
        message="Add this host to SSH config?",
        default=True,
    ).execute()

    if not save:
        return

    while True:
        config_name = inquirer.text(
            message="Enter a name for this host:",
        ).execute().strip()

        if not config_name:
            print("\nHost name cannot be empty.")
            continue

        if config_name in get_ssh_hosts():
            print(f"\nHost '{config_name}' already exists. Choose another name.")
            continue

        add_manual_host_to_config(target, config_name)
        break

def ssh(host):
    subprocess.run(
        ["ssh", host],
        check=True,
    )


def main():
    hosts = get_ssh_hosts()

    while True:
        clear()
        host, is_manual = choose_host(hosts)

        while True:
            print(f"\nConnecting to {host}...\n")

            try:
                ssh(host)

                if is_manual:
                    ask_to_save_manual_host(host)
                break  # Success: exit launcher.
            except subprocess.CalledProcessError as e:
                print(f"\nSSH exited with status {e.returncode}.")
            except FileNotFoundError:
                print("\nError: ssh executable not found.")
                return
            except KeyboardInterrupt:
                print("\nCancelled.")
                return

            retry = inquirer.confirm(
                message=f"Retry connecting to '{host}'?",
                default=True,
            ).execute()

            if not retry:
                break  # Go back to host selection.


if __name__ == "__main__":
    main()