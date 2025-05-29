import requests

teveclubUrl = "https://www.teveclub.hu"

def test_teveclub_sanity_check():
    print("\nStarting Sanity Check for Teveclub")
    try:
        response = requests.get(teveclubUrl)
        print(f"\nSanity check response: {response}")
        assert response.status_code == 200
        print("Sanity check passed, moving to the UI tests")
    except requests.exceptions.RequestException as errorMsg:
        print("Teveclub is unreachable:", errorMsg)
        assert False

