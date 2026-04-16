from src.ramonavocado_logger.logger import get_log
from src.ramonavocado_logger.wrapper import toggle_log

log = get_log(test="True")

@toggle_log(False)
def silent_func():
    log.info("you will NOT see this")


@toggle_log(True)
def noisy_func():
    log.info("you WILL see this")

def main():
    silent_func()
    silent_func()
    silent_func()
    noisy_func()


if __name__ == "__main__":
    main()


