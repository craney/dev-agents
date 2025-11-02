# TDD 代理使用示例

本文档演示如何在Claude Code中使用TDD相关代理进行测试驱动开发工作流。

## TDD 编排代理

`tdd-orchestrator` 代理管理完整的TDD工作流，协调多个专业化代理。

### 基本用法

```bash
# 为新功能调用TDD编排器
使用Task工具，subagent_type="tdd-orchestrator"
提示："使用TDD方法和JWT令牌实现用户身份验证"

# 编排器将：
# 1. 分析需求并设计测试策略
# 2. 与test-automator协调进行测试创建
# 3. 管理红-绿-重构循环
# 4. 跟踪指标并确保TDD合规性
```

### 高级编排

```bash
# 多团队TDD协调
使用Task工具，subagent_type="tdd-orchestrator"
提示："协调前端、后端和移动团队的购物车功能TDD工作流"

# 基于属性的TDD
使用Task工具，subagent_type="tdd-orchestrator"
提示："使用基于属性的TDD和不变量检查实现排序算法"

# 遗留代码TDD
使用Task工具，subagent_type="tdd-orchestrator"
提示："在重构前为遗留PaymentProcessor类添加测试，使用特征测试"
```

## 具有TDD能力的测试自动化器

增强的`test-automator`代理现在包含全面的TDD支持。

### 测试优先开发

```bash
# 首先生成失败测试
使用Task工具，subagent_type="test-automator"
提示："为带有电子邮件验证的用户注册生成全面的失败测试。确保测试因正确原因失败。"

# 增量测试开发
使用Task工具，subagent_type="test-automator"
提示："为购物车创建增量测试套件：从添加商品开始，然后移除，最后计算总计"

# 基于属性的TDD测试
使用Task工具，subagent_type="test-automator"
提示："使用hypothesis/fast-check为字符串工具库生成基于属性的测试"
```

### TDD指标和合规性

```bash
# 跟踪TDD指标
使用Task工具，subagent_type="test-automator"
提示："分析代码库并生成TDD合规性报告：测试优先百分比、周期时间、重构频率"

# 验证TDD纪律
使用Task工具，subagent_type="test-automator"
提示："检查最近的提交是否遵循TDD：在实现之前编写测试"
```

## 特定语言的TDD示例

### Python TDD

```bash
使用Task工具，subagent_type="python-pro"
提示："使用pytest和TDD方法实现二叉搜索树。从插入、搜索、删除操作的失败测试开始。"

使用Task工具，subagent_type="test-automator"
提示："为REST API生成Python pytest测试，使用TDD：先写契约测试，然后单元测试，遵循芝加哥学派TDD"
```

### JavaScript/TypeScript TDD

```bash
使用Task工具，subagent_type="typescript-pro"
提示："使用Jest和React Testing Library通过TDD构建React组件。从行为测试开始，然后最小化实现。"

使用Task工具，subagent_type="javascript-pro"
提示："使用Mocha和Chai通过TDD方法实现Express中间件。使用模拟的伦敦学派方法。"
```

### Java TDD

```bash
使用Task工具，subagent_type="java-pro"
提示："使用JUnit 5和Mockito通过TDD创建Spring Boot服务。从集成测试开始，然后单元测试。"
```

### Go TDD

```bash
使用Task工具，subagent_type="golang-pro"
提示："使用Go的testing包和testify通过TDD方法构建gRPC服务。包括表驱动测试。"
```

## TDD工作流模式

### 经典红-绿-重构

```bash
# 步骤1：红色 - 编写失败测试
使用Task工具，subagent_type="test-automator"
提示："为处理负数的斐波那契函数编写失败测试"

# 步骤2：绿色 - 最小实现
使用Task工具，subagent_type="python-pro"
提示："实现最小斐波那契函数使测试通过"

# 步骤3：重构 - 改进代码
使用Task工具，subagent_type="code-reviewer"
提示："重构斐波那契实现以提高性能，同时保持测试绿色"
```

### 由外向内TDD（伦敦学派）

```bash
# 从验收测试开始
使用Task工具，subagent_type="test-automator"
提示："使用Cucumber/Gherkin为用户登录流程编写验收测试"

# 使用模拟向内工作
使用Task工具，subagent_type="test-automator"
提示："为带有模拟依赖项的登录控制器编写单元测试"

# 使用TDD实现
使用Task工具，subagent_type="backend-architect"
提示："实现登录控制器以满足测试，使用依赖注入"
```

### 由内向外TDD（芝加哥学派）

```bash
# 从单元测试开始
使用Task工具，subagent_type="test-automator"
提示："为单个计算函数编写单元测试"

# 构建到集成
使用Task工具，subagent_type="test-automator"
提示："编写结合计算函数的集成测试"

# 最终验收测试
使用Task工具，subagent_type="test-automator"
提示："为完整计算工作流编写端到端测试"
```

## 专业化TDD场景

### API开发与TDD

```bash
使用Task工具，subagent_type="tdd-orchestrator"
提示："
通过TDD开发博客平台REST API：
1. 从OpenAPI规范开始
2. 从规范生成契约测试
3. 测试优先实现端点
4. 添加集成测试
5. 包含性能测试
"
```

### 微服务TDD

```bash
使用Task工具，subagent_type="tdd-orchestrator"
提示："
通过TDD方法构建微服务：
- API的契约测试
- 业务逻辑的单元测试
- 数据库的集成测试
- 服务的组件测试
- 工作流的端到端测试
"
```

### 前端组件TDD

```bash
使用Task工具，subagent_type="frontend-developer"
提示："
通过TDD构建日期选择器组件：
1. 测试组件渲染
2. 测试日期选择
3. 测试键盘导航
4. 测试可访问性
5. 测试日期验证
所有测试优先，然后实现
"
```

### 数据库迁移TDD

```bash
使用Task工具，subagent_type="database-optimizer"
提示："
通过TDD执行数据库迁移：
1. 为当前模式行为编写测试
2. 为期望的模式行为编写测试
3. 实现迁移以通过两者
4. 包含回滚测试
"
```

## TDD反模式检测

```bash
# 检测开发后测试
使用Task工具，subagent_type="code-reviewer"
提示："审查最近的提交并识别测试在实现后编写的位置"

# 查找过度模拟的测试
使用Task工具，subagent_type="test-automator"
提示："分析测试套件并识别具有过度模拟而不测试真实行为的测试"

# 识别缺失的测试覆盖
使用Task工具，subagent_type="test-automator"
提示："查找没有测试的代码路径并建议遵循TDD方法的测试用例"
```

## TDD指标和报告

```bash
# 生成TDD仪表板
使用Task工具，subagent_type="tdd-orchestrator"
提示："创建显示以下内容的TDD指标仪表板：周期时间、测试优先百分比、重构频率、覆盖率趋势"

# 团队TDD评估
使用Task工具，subagent_type="tdd-orchestrator"
提示："评估团队的TDD成熟度级别并提供改进建议"

# TDD ROI分析
使用Task工具，subagent_type="business-analyst"
提示："计算采用TDD的投资回报率：错误减少、开发速度、维护成本"
```

## TDD学习和训练

```bash
# TDD训练练习
使用Task工具，subagent_type="tdd-orchestrator"
提示："使用严格的TDD指导我完成罗马数字训练"

# TDD工作坊材料
使用Task工具，subagent_type="tdd-orchestrator"
提示："创建包含团队训练练习的TDD工作坊"

# TDD代码审查
使用Task工具，subagent_type="code-reviewer"
提示："审查此代码的TDD最佳实践并提供具体改进建议"
```

## 与CI/CD集成

```bash
# TDD管道设置
使用Task工具，subagent_type="deployment-engineer"
提示："设置强制执行TDD的CI/CD管道：验证在代码之前编写测试，检查覆盖率，跟踪指标"

# 提交前TDD钩子
使用Task工具，subagent_type="dx-optimizer"
提示："创建确保在允许提交前TDD合规性的git钩子"
```

## 不同架构的TDD

### 六边形架构与TDD

```bash
使用Task工具，subagent_type="architect-review"
提示："通过TDD实现六边形架构服务：从域测试开始，然后端口，然后适配器"
```

### 事件驱动TDD

```bash
使用Task工具，subagent_type="tdd-orchestrator"
提示："通过TDD构建事件驱动系统：测试事件生产、消费和编排"
```

### 无服务器TDD

```bash
使用Task工具，subagent_type="cloud-architect"
提示："通过TDD方法开发Lambda函数，包括本地测试和集成测试"
```

## 常见TDD命令组合

### 完整TDD功能开发

```bash
# 1. 使用编排器设计测试
使用Task工具，subagent_type="tdd-orchestrator"
提示："为支付处理功能设计全面的测试策略"

# 2. 使用自动化器生成测试
使用Task工具，subagent_type="test-automator"
提示："生成策略中识别的所有测试用例"

# 3. 使用语言专家实现
使用Task工具，subagent_type="python-pro"
提示："增量实现支付处理以通过测试"

# 4. 审查和重构
使用Task工具，subagent_type="code-reviewer"
提示："审查实现并建议重构，同时保持绿色测试"

# 5. 优化性能
使用Task工具，subagent_type="performance-engineer"
提示："使用TDD方法优化支付处理性能"
```

### TDD错误修复工作流

```bash
# 1. 用测试重现
使用Task工具，subagent_type="test-automator"
提示："编写重现错误#123的测试：用户无法使用特殊字符登录"

# 2. 最小修复
使用Task工具，subagent_type="debugger"
提示："通过最小更改修复错误使测试通过"

# 3. 添加边缘情况
使用Task工具，subagent_type="test-automator"
提示："为与错误相关的边缘情况添加其他测试用例"

# 4. 如需要则重构
使用Task工具，subagent_type="code-reviewer"
提示："建议重构以防止类似错误"
```

## 代理使用最佳实践

1. **从tdd-orchestrator开始**，用于需要协调的复杂功能
2. **使用test-automator**进行测试生成和验证
3. **利用特定语言代理**进行实现阶段
4. **雇用code-reviewer**进行重构阶段
5. **使用business-analyst跟踪**指标和ROI

## 故障排除

### 当测试不失败时

```bash
使用Task工具，subagent_type="test-automator"
提示："验证当实现被移除时这些测试实际上失败（变异测试）"
```

### 当TDD感觉慢时

```bash
使用Task工具，subagent_type="tdd-orchestrator"
提示："优化TDD工作流以获得更快的反馈循环"
```

### 当团队抵制TDD时

```bash
使用Task工具，subagent_type="tdd-orchestrator"
提示："为团队创建渐进式TDD采用计划，包含培训材料"
```

## 高级TDD技术

### 批准测试

```bash
使用Task工具，subagent_type="test-automator"
提示："为复杂输出验证设置批准测试"
```

### 快照测试

```bash
使用Task工具，subagent_type="test-automator"
提示："使用TDD为UI组件实现快照测试"
```

### 契约测试

```bash
使用Task工具，subagent_type="test-automator"
提示："使用Pact和TDD方法在服务之间创建契约测试"
```

## 下一步

1. 尝试[TDD工作流命令](/workflows:tdd-cycle)
2. 使用tdd-orchestrator练习TDD训练
3. 将TDD代理集成到您的开发工作流中
4. 使用test-automator跟踪TDD指标
5. 与您的团队分享TDD成功故事