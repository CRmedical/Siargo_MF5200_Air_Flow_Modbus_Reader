import argparse
from sensor import Sensor


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="flow-reader",
        description="CLI para leitura de sensor de fluxo de ar",
    )

    parser.add_argument(
        "--port",
        type=str,
        required=True,
        help="Porta serial do sensor (ex: COM5, /dev/ttyUSB0)",
    )

    parser.add_argument(
        "--address",
        type=int,
        required=True,
        help="Endereço Modbus do sensor",
    )

    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    try:
        sensor = Sensor(args.port, args.address)

        accumulated = sensor.get_accumulated_flow()
        rate = sensor.get_intent_flow_rate()

        print(f"Accumulated Flow : {accumulated}")
        print(f"Instant Flow Rate: {rate}")

    except Exception as e:
        print(f"Erro ao comunicar com o sensor: {e}")


if __name__ == "__main__":
    main()