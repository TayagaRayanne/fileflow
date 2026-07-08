from core.config_loader import ConfigLoader


def main():
    loader = ConfigLoader()
    config = loader.load()

    print(config)


if __name__ == "__main__":
    main()