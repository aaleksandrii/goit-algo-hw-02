from queue import Queue


queue = Queue()

def generate_request(id: int) -> None:
    request = f"Request: {id}"
    queue.put(request)
    print(f"Generated: '{request}'")

def process_request() -> None:
    if not queue.empty():
        request = queue.get()
        print(f"Handling: '{request}'")
    else:
        print("No requests to process")

def main():
    request_count = 4

    # creating part
    for i in range(1, request_count):
        generate_request(i)
    print()

    # reading part (plus one extra case)
    for i in range(request_count):
        process_request()

if __name__ == "__main__":
    main()
