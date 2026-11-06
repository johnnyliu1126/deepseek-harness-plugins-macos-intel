# Browser tool reference / 浏览器工具逐项说明

`dsh-ego-browser` 0.9.8. This list is grounded in the installed runtime help table and tool definitions, not inferred from the package name. / 对照已安装运行时帮助表与工具定义，不按包名猜测。

| Tool | 中文 | English |
|---|---|---|
| `ego_status` | 检查 CLI 和浏览器状态 | Check CLI/browser availability |
| `ego_space_open` | 打开任务空间 | Open a task space |
| `ego_space_close` | 关闭任务空间 | Close a task space |
| `ego_snapshot` | 读取页面语义树与定位引用 | Read semantic tree and locator references |
| `ego_navigate` | 导航 URL 或复用标签页 | Navigate to a URL or reuse a tab |
| `ego_tabs` | 列出、切换、新建、关闭标签页 | List, switch, open and close tabs |
| `ego_click` | 点击或双击元素/坐标 | Click/double-click an element or coordinate |
| `ego_fill` | 填写输入框 | Fill an input |
| `ego_js` | 执行页面 JavaScript | Evaluate page JavaScript |
| `ego_cdp` | 发送 Chrome DevTools 命令 | Send Chrome DevTools commands |
| `ego_screenshot` | 页面或元素截图 | Capture a page or element screenshot |
| `ego_page_info` | 读取标题、视口、滚动、弹窗和验证状态 | Read title, viewport, scrolling, dialogs and human-check state |
| `ego_wait` | 等待固定时间 | Wait a fixed duration |
| `ego_wait_for_selector` | 等待元素出现或消失 | Wait for an element to appear/disappear |
| `ego_wait_for_url` | 等待页面跳转 | Wait for URL navigation |
| `ego_wait_for_response` | 等待网络响应并读取响应体 | Wait for/read a network response |
| `ego_wait_for_human` | 等待用户完成登录或人工验证 | Wait for the user to complete login/verification |
| `ego_key` | 按键组合或连续输入 | Press key combinations or type text |
| `ego_hover` | 鼠标悬停 | Hover |
| `ego_read_element` | 读取文本、HTML、属性、值和可见性 | Read text, HTML, attributes, value and visibility |
| `ego_select` | 选择下拉选项 | Select an option |
| `ego_drag` | 拖动元素或坐标 | Drag elements or coordinates |
| `ego_scroll` | 滚动页面或定位元素 | Scroll or bring an element into view |
| `ego_upload` | 上传本地文件 | Upload local files |
| `ego_check` | 勾选或取消选择 | Check/uncheck controls |
| `ego_dialog` | 处理 JavaScript 对话框 | Handle JavaScript dialogs |
| `ego_download` | 等待下载并保存到指定路径 | Wait for a download and save it |
| `ego_http` | 浏览器或 Node 上下文 HTTP 请求 | Issue browser-context or Node HTTP requests |
| `ego_captcha` | 检测验证码类型，交给用户完成 | Detect CAPTCHA type for user completion |
| `ego_auth_flush` | 将浏览器登录 Cookie 保存到本地 profile | Persist login cookies into the local browser profile |
| `ego_login_import` | 通过扩展或副本导入指定域名登录状态 | Import domain-scoped login state through a bridge/copy |
| `ego_help` | 查看分类帮助和工具索引 | Read categorized help and the tool index |
| `ego_doctor` | 检查浏览器、运行时、端口和空间 | Diagnose browser/runtime/ports/spaces |
| `ego_cli` | 运行 ego 运行时脚本 | Run an ego runtime script |
| `ego_script` | 运行脚本并返回耗时与超时状态 | Run a script with duration/timeout metadata |

These tools act on a real browser and filesystem. Upload/download, credential import and arbitrary scripts require deliberate selection of data and destination. CAPTCHA detection is not a claim of automatic solving. The collection does not import any cookies or run browser scripts during release verification. / 工具操作真实浏览器与文件；上传下载、登录导入和任意脚本需明确数据和目标。验证码检测不等于自动解答。本次发布验证未导入 Cookie 或运行浏览器脚本。
