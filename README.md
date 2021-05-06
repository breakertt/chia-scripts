# chia-scripts

Please translate by yourself if you are not a Chinese speaker.

## 功能
- NUMA 绑定
- 自动 SSD -> HDD 分配
- 延迟启动

## 使用
学生，没空提供技术支持，得自己打开源码改

## 未来规划

- 下一个版本（全新重构）
  - 主脚本
    1. 确定 ssd 和并行数量
    2. 调用 tmux 运行副脚本
  - 副脚本（tmux 内）
    1. 自动轮回
    2. 启动 p 盘
    3. 自动确定一个目的地
    4. 自动延时
    5. 自动停止轮回

- 下下个版本（监控中台）：
  实现一个专门提供集聚显示的监控中台，其中每个副脚本进程会实时汇报目前状态和最后p完文件的幸运值
