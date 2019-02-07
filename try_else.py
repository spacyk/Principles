
def try_else_test(division_number):
    try:
        output = 10/division_number
    except ZeroDivisionError:
        print("you can\'t divide with Zero")
    else:
        # Also can throw some other error that maybe we don't want to catch
        print(f"Division was successful, the value is: {output}")
    finally:
        print("Done")


if __name__ == "__main__":
    try_else_test(2)