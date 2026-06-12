# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-06-12

### Added
- Initial release of the **trading-strategy-review** Agent Skill.
- `skill.md` methodology: When to Activate, Scope & Context, a Critical→Info severity model,
  a 16-mode failure checklist (look-ahead, survivorship, overfitting, multiple testing,
  unrealistic fills, slippage/commission, market impact, regime dependence, no OOS/walk-forward,
  position sizing & risk-of-ruin, leverage & path dependence, funding/borrow, timezone/session,
  repainting, curve-fit exits, too-few-trades), a red-flag quick scan, an output format, a
  metrics sanity check (Sharpe, Sortino, max drawdown, Deflated Sharpe, PBO), and a
  not-financial-advice disclaimer.
- Grounding in the Bailey & López de Prado backtest-overfitting literature (PBO, Deflated
  Sharpe Ratio, The Seven Sins of Quantitative Investing).
- Two worked example reports: `examples/ma-crossover-review.md` and `examples/pine-rsi-review.md`.
- README with install, usage, features, red-flag thresholds, and cross-links to `bar-by-bar`
  and `edgehunt`.
- CI validator (`scripts/validate_skill.py`) and GitHub Actions workflow.

[1.0.0]: https://github.com/Viprasol-Tech/trading-strategy-review/releases/tag/v1.0.0
