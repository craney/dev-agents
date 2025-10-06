# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库概述

这是一个包含83个专业化AI子代理的集合，专为Claude Code设计，提供软件开发、基础设施和业务运营等领域的域专业知识。每个子代理都以Markdown文件定义，包含名称、描述、模型分配和工具限制等元数据。

## 架构结构

### 子代理格式
每个代理遵循以下格式：
```markdown
---
name: agent-name
description: 该子代理的激活条件
model: haiku|sonnet|opus  # 可选：模型选择
tools: tool1, tool2       # 可选：工具限制
---

定义子代理专业知识和行为的系统提示
```

### 模型分配策略
- **haiku**: 简单、确定性任务，最少推理需求（11个代理）
- **sonnet**: 标准开发和工程任务（46个代理）
- **opus**: 复杂分析、架构设计和关键操作（22个代理）

### 代理分类
- **架构与系统设计**: 核心架构、UI/UX、移动开发
- **编程语言**: 18个特定语言代理，涵盖系统、Web、企业和专业平台
- **基础设施与运维**: DevOps、数据库管理、事件响应、网络
- **质量保证与安全**: 代码审查、安全审计、测试、性能、可观测性
- **数据与AI**: 数据工程、机器学习、AI工程
- **文档与技术写作**: 综合文档和教程创建
- **业务与运营**: 业务分析、财务、营销、支持、法务
- **SEO与内容优化**: 10个专业化SEO代理
- **专业领域**: 区块链、支付、遗留系统现代化

## 开发流程

### 添加新代理
1. 创建新的`.md`文件，使用小写连字符分隔的命名
2. 包含适当的frontmatter：名称、描述和可选的模型/工具
3. 编写包含8-12个专业领域的综合系统提示
4. 更新README.md，将新代理包含在相应的分类表格中

### 代理激活
- **自动**: Claude Code分析请求上下文并选择最优代理
- **显式**: 通过名称指定代理（例如："使用code-reviewer分析更改"）
- **多代理工作流**: 代理自动协调处理复杂任务

### 安装过程
```bash
cd ~/.claude
git clone https://github.com/wshobson/agents.git
```

## 关键文件

- `README.md`: 包含代理分类和使用示例的综合文档
- 各个代理文件: 每个文件包含专业知识和激活条件
- 无构建系统、测试或包管理器 - 这是一个文档仓库

## 代理选择指南

### 架构任务
- `backend-architect`: REST/GraphQL API、微服务、数据库架构
- `cloud-architect`: AWS/Azure/GCP基础设施设计
- `kubernetes-architect`: 基于GitOps的云原生基础设施

### 开发任务
- 特定语言代理: `javascript-pro`、`python-pro`、`java-pro`等
- `frontend-developer`: React组件、响应式布局
- `mobile-developer`: React Native和Flutter开发

### 质量与安全
- `code-reviewer`: 专注安全的代码审查
- `security-auditor`: 漏洞评估和OWASP合规性
- `performance-engineer`: 应用程序性能分析和优化

### 运维
- `devops-troubleshooter`: 生产环境调试和日志分析
- `incident-responder`: 生产环境事件管理
- `terraform-specialist`: 基础设施即代码

## 最佳实践

- 信任自动代理选择以获得最佳专业知识匹配
- 委托任务时提供清晰的上下文和需求
- 对特定专业知识需求使用显式代理调用
- 利用多代理工作流处理复杂的多领域任务
- 监控代理效果并根据反馈优化需求