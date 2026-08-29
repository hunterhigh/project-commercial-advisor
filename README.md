# Project Commercial Advisor

一个通用的项目商业顾问插件。它在立项前形成可验证的商业判断，并在项目上线后使用真实经营结果检验和修正判断，帮助用户决定立项、继续、调整、追加投入、降低投入、暂停或停止。

## 边界

- 分析对象是项目作为一项商业投入，不是章节文本。
- 不评价小说段落是否好看，不承担编辑或改写。
- 不使用固定商业评分，也不把公开代理指标冒充订阅、收入或因果证据。
- 不运行定时任务、爬虫、数据库或自动登录。
- 平台规则和市场数据只在用户咨询时按需核验。

首版提供起点平台的轻量来源入口，以及章节更新和利润模型的确定性计算器。

## 独立克隆

```powershell
git clone https://github.com/hunterhigh/project-commercial-advisor.git
```

本仓库也是 `ruwen-v5` 的 Git submodule，但不依赖 Ruwen 的运行代码。

## 验证

```powershell
$env:PYTHONUTF8 = "1"
python -m unittest discover -s tests -p "test_*.py"
python C:\Users\admin\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\skills\project-commercial-advisor
python C:\Users\admin\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .
```
