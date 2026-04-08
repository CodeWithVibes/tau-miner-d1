#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

import bittensor as bt


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Publish an SN66 miner commitment with the Bittensor Python SDK."
    )
    parser.add_argument("--wallet-name", required=True, help="Cold wallet name")
    parser.add_argument("--wallet-hotkey", required=True, help="Hotkey name")
    parser.add_argument("--netuid", type=int, default=66, help="Subnet netuid")
    parser.add_argument("--data", required=True, help="Commitment string like owner/repo@sha")
    parser.add_argument(
        "--network",
        default=None,
        help="Optional Bittensor network name or endpoint",
    )
    parser.add_argument(
        "--wallet-path",
        default=None,
        help="Optional wallet path. Defaults to the SDK standard wallet directory.",
    )
    parser.add_argument(
        "--no-wait",
        action="store_true",
        help="Return after submission instead of waiting for inclusion/finalization.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    encoded = args.data.encode()

    if len(encoded) > 128:
        print(
            f"commitment is too long for Raw0-128 metadata: {len(encoded)} bytes",
            file=sys.stderr,
        )
        return 1

    wallet = bt.Wallet(
        name=args.wallet_name,
        hotkey=args.wallet_hotkey,
        path=args.wallet_path,
    )
    subtensor = bt.Subtensor(network=args.network) if args.network else bt.Subtensor()

    response = subtensor.set_commitment(
        wallet=wallet,
        netuid=args.netuid,
        data=args.data,
        wait_for_inclusion=not args.no_wait,
        wait_for_finalization=not args.no_wait,
    )

    print(f"submitted={args.data}")
    print(f"netuid={args.netuid}")
    print(f"network={getattr(subtensor, 'network', 'unknown')}")

    success = bool(getattr(response, "success", False))
    print(f"success={success}")

    block_hash = getattr(response, "block_hash", None)
    if block_hash:
        print(f"block_hash={block_hash}")

    if not success:
        error = getattr(response, "error", None) or getattr(response, "message", None)
        if error:
            print(f"error={error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
