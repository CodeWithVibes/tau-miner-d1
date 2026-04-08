# tau-miner-d1

`tau-miner-d1` is a submit-ready SN66 challenger repo tuned for SN66's positional diff scoring.

The public Tau validator currently clones a miner repo and then looks for the runnable workspace in `agent/`, so this project keeps the full PI agent workspace there instead of at the repo root.

## Why this repo is different

- It keeps the validator-compatible `agent/` layout.
- It uses a custom `agent/.pi/SYSTEM.md` so the runtime prompt is focused on diff matching instead of the broader default PI prompt.
- It uses a tighter `agent/AGENTS.md` focused on acceptance-criteria coverage, minimal diffs, and positional diff safety.
- It strips project-local `.pi` extensions and prompt templates that are useful interactively but noisy for validator solves.

## Local eval loop

From the main Tau repo:

```bash
cd /root/tau
source .venv/bin/activate

tau generate --task demo-task
tau solve --task demo-task --solution cursor --agent cursor
tau solve --task demo-task --solution challenger --agent /root/tau-miner-d1/agent
tau compare --task demo-task --solutions cursor challenger
tau eval --task demo-task --solutions cursor challenger
```

That gives you a quick read on whether this agent is tracking the Cursor baseline well on locally generated tasks.

## Publish

```bash
cd /root/tau-miner-d1
git init
git add .
git commit -m "Add SN66 challenger miner"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/tau-miner-d1.git
git push -u origin main
```

## Build the on-chain submission string

After your first push, run:

```bash
cd /root/tau-miner-d1
./scripts/submission-ref.sh YOUR_GITHUB_USERNAME/tau-miner-d1
```

It prints:

- `submission_ref=owner/repo@full_commit_sha`
- `commit_url=https://github.com/owner/repo/commit/full_commit_sha`

Use the `submission_ref` value as the commitment text for subnet 66.

## Commit it on-chain

This machine does not have the Bittensor CLI installed, but the Tau virtualenv already includes the Python SDK method that the validator uses on the read side.

```bash
source /root/tau/.venv/bin/activate
cd /root/tau-miner-d1
python ./scripts/set_commitment.py \
  --wallet-name YOUR_WALLET_NAME \
  --wallet-hotkey YOUR_HOTKEY \
  --netuid 66 \
  --network finney \
  --data "$(./scripts/submission-ref.sh YOUR_GITHUB_USERNAME/tau-miner-d1 | sed -n 's/^submission_ref=//p')"
```

Then verify the submission is visible:

```bash
cd /root/tau
source .venv/bin/activate
tau submissions --netuid 66
```
