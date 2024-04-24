import etcd3
import os


def connect_to_etcd(host, port):

    try:
        etcd_client = etcd3.client(host=host, port=port)
        etcd_client.status()
        print("Connected to etcd successfully.")
        return etcd_client
    except etcd3.exceptions.ConnectionFailedError as e:
        print(f"Connection to etcd failed in connect_to_etcd: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_all_etcd_keys(etcd_client):

    try:
        keys = etcd_client.get_all()

        key_list = [m.key.decode('utf-8') for (_, m) in keys]

        return key_list
    except etcd3.exceptions.ConnectionFailedError as e:
        print(f"Connection to etcd failed in get_all_etcd_keys: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return []


def get_etcd_key_value(etcd_client, key):

    try:
        value, metadata = etcd_client.get(key)

        if value is None:
            print(f"Key '{key}' does not exist.")
            return None
        return value.decode('utf-8')

    except etcd3.exceptions.ConnectionFailedError as e:
        print(f"Connection to etcd failed in get_etcd_key_value: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return None


def insert_etcd_key_value(etcd_client, key, value):

    try:
        etcd_client.put(key, value)
        print(f"Inserted key '{key}' with value '{value}' successfully.")
        return True
    except etcd3.exceptions.ConnectionFailedError as e:
        print(f"Connection to etcd failed in insert_etcd_key_value: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return False

def delete_etcd_key(etcd_client, key):

    if etcd_client:
        try:
            deleted = etcd_client.delete(key)
            if deleted:
                print(f"Deleted key '{key}' successfully.")
                return True
            else:
                print(f"Key '{key}' does not exist.")
                return False
        except Exception as e:
            print(f"Error: {e}")
    return False



if __name__ == "__main__":

        etcd_client = connect_to_etcd("localhost",1111)
        if etcd_client is not None:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select an operation:")
                print("1. Get all keys")
                print("2. Get value for a key")
                print("3. Insert a key-value pair")
                print("4. Delete a key")
                print("5. Change ETCD node")
                print("0. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    key_list = get_all_etcd_keys(etcd_client)
                    print(key_list)
                elif choice == "2":
                    key = input("Enter the key: ")
                    value = get_etcd_key_value(etcd_client, key)
                    if value is not None:
                        print(f"Value for key '{key}': {value}")
                elif choice == "3":
                    key = input("Enter the key: ")
                    value = input("Enter the value: ")
                    success = insert_etcd_key_value(etcd_client, key, value)
                elif choice == "4":
                    key = input("Enter the key: ")
                    success = delete_etcd_key(etcd_client, key)
                elif choice == "5":
                    port = input("VALID PORTS=[22379,32379]\nEnter Port Number: ")
                    success = connect_to_etcd("localhost",int(port))
                elif choice == "0":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")

                input("Press Enter to continue...")