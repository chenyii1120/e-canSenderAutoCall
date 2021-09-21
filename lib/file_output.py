
def print_crash_report(status):
    print(status.crash_info)
    report_path = f"CrashReport/{status.get_report_time_inform()}.txt"
    with open(report_path, mode="w") as crash_report:
        crash_report.write(status.crash_info)
    print(f"The Crash Report has saved in path: {report_path}")
    raise Exception("")

def print_log(status):

    if status.result:
        msg = "Success"
    else:
        msg = "Fail"

    print(f"Status: {msg}")
    with open("log.txt", mode="a") as file:
        file.write(f"{status.get_now_inform()}\t{msg}\n")