# 开发计划

## 核心玩法

1. 待定
2. 待定
3. 待定

---

## MAP

### 颜色 & 图层系统

- [x] **创建颜色枚举** — `Color` 枚举定义在 `picture/color.py`，支持黑/红/绿/黄/蓝/紫/青/白
- [x] **染色函数实现** — `set_color()` 基于 ANSI escape code，已在屏幕绘制中生效
- [x] **图层类 `Layer`** — 每个 Layer 持有一个 `list[str]` 层内容 + `Color`，支持改色
- [x] **多层叠加绘制** — `Picture` 支持多个 `Layer` 叠加，按添加顺序依次绘制（后层覆盖前层）
- [x] **`Layer` 色彩传递到 `Screen`** — `draw()` 中已完整传递 `Layer.color` → `set_color()` → 终端

### Bug 修复

- [x] **绘制空格跳过** — Layer 中 `" "` 跳过不覆盖，`None` 擦除为空格
- [x] **修复 `= vs ==` bug** — `screen.py` 中将 None 擦除的逻辑误用 `==` 判等，改为赋值
- [x] **修复 `is` 字符串比较** — 空格判断改用 `==` 而非 `is`
- [x] **修复 `have_new_frame` 语义混乱** — 拆分 bool/Frame 双重语义，改用 `_frame: Optional[GameFrame]`
- [x] **修复 `map_class` 导入与继承** — 错误 import 和错误的父类构造参数
- [x] **修复拼写错误** — `qiuck_refresh` → `quick_refresh`，`creat_map.py` 已删除

### 代码质量

- [x] **添加类型注解** — 所有函数/方法参数和返回值均标注类型
- [x] **添加 `__init__.py`** — `picture/` 和 `picture/map/` 改为正规包
- [x] **删除死代码** — `Picture.sharp`、`init_sharp()`、空文件 `creat_map.py`
- [x] **`config.py` 改用 dataclass** — `InitConfig` 使用 `@dataclass` 简写
- [x] **修正命名字典** — `GetKey()` → `get_key()` 符合 PEP 8

### 框架优化

- [ ] **提取 `GameFrame.draw`** — 将 `draw` 逻辑从 `GameFrame` 中独立出来，或重构为独立的 renderer
- [ ] **外层框分离** — 将最外层的 `/—\` 边框用单独一帧绘制，不硬编码在 `GameScreen.refresh()` 中（边框不一定为矩形）
- [ ] **单字符彩色层透明混合** — 当前 `Layer` 换行符长度不一致时用空格填充，未来考虑任一位置可直接透明或着色

### 玩法开发

- [ ] **将牌框与牌面分别保存** — 卡牌系统的基础数据结构（等待玩法设计）
- [ ] **核心玩法** — 待定（三个坑位等待填充）

### 远期思考

- [ ] **异步输入** — 游戏主循环需要非阻塞键盘输入，而非 `input()` 阻塞
- [ ] **屏幕缓冲区优化** — 仅刷新变化区域，减少全屏 `clear` 闪烁
