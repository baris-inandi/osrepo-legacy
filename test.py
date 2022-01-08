from modules import cli
from pprint import pprint

if __name__ == "__main__":
    test_result = {
        'download from search result': cli.search_os("templeos"),
        'download with id': cli.download_with_id("templeos@latest"),
    }
    failed = []
    for k in test_result.items():
        try:
            test_name, test_result = k[0], k[1]
            print("PASSED:", test_result["url"], test_result["browser"])
        except Exception as e:
            print("TEST FAILED:", k)
            print("WITH EXCEPTION", e)
            failed.append({"data": k, "exception": e})
    if failed:
        print()
        for f in failed:
            pprint(f)
    else:
        print("\nALL TESTS PASSED")
