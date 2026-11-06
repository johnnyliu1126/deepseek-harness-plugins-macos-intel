/**
 * dsh-restart —— Client 半区
 *
 * 入口**常驻**在侧边栏页脚、账号那一行的上方：一个标签（一键重启）+ 一行说明
 * （重启 DSH 服务）+ 右侧「重启」按钮。比原来那个孤零零的圆形箭头多两样东西 ——
 * 文字标签和说明，不用点开、不用悬停也知道它是干嘛的。
 *
 * 侧边栏收成 56px 竖条（wide=false）时文字放不下，退化成和其余页脚图标同尺寸的按钮，
 * 完整说明放在 title/aria-label 里。
 *
 * 点「重启」→ POST /dsh-restart/restart → 按钮进入「重启中…」→ 轮询宿主，
 * 等它挂掉又回来时刷新页面（浏览器场景；桌面版窗口会跟着应用一起重启）。
 */

window.__ModuleLoader__.load({
  id: 'dsh-restart',
  factory(require) {
    const React = require('react')
    const h = React.createElement
    const { useCallback, useEffect, useRef, useState } = React

    const STYLE_ID = 'dsh-restart-style'
    const HINT = '重启 DSH 服务；重启期间本页面会自动重新连接。'
    const POLL_MS = 700
    const POLL_LIMIT = 120

    const CSS = `
.dshr-card{
  display:flex;align-items:center;gap:8px;
  flex:1;min-width:0;box-sizing:border-box;
  padding:2px 2px 2px 8px;
}
.dshr-icon{display:block;width:14px;height:14px}
@keyframes dshr-spin{to{transform:rotate(360deg)}}
.dshr-text{display:flex;flex-direction:column;flex:1;min-width:0;gap:1px}
.dshr-title{
  font-size:13px;font-weight:500;line-height:17px;
  color:var(--dsw-alias-label-primary);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}
.dshr-sub{
  font-size:11px;line-height:15px;
  color:var(--dsw-alias-label-tertiary);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}
.dshr-sub[data-tone="error"]{color:var(--dsw-alias-state-error-primary)}
.dshr-action{
  appearance:none;flex:none;
  display:inline-flex;align-items:center;justify-content:center;
  height:26px;padding:0 10px;
  border:0;border-radius:var(--dsw-radius-sm);
  background:var(--dsw-alias-bg-module-platform);
  color:var(--dsw-alias-label-primary);
  font:inherit;font-size:12px;line-height:18px;font-weight:500;
  cursor:pointer;white-space:nowrap;
  transition:background-color .12s,opacity .12s;
}
@media (hover:hover){.dshr-action:hover:not(:disabled){background:var(--dsw-alias-interactive-bg-hover)}}
.dshr-action:disabled{opacity:.6;cursor:default}
.dshr-action[data-busy="true"]{color:var(--dsw-alias-label-secondary)}
.dshr-rail{
  appearance:none;flex:none;display:inline-flex;align-items:center;justify-content:center;
  width:36px;height:36px;padding:0;border:0;border-radius:var(--dsw-radius-md);
  background:transparent;color:var(--dsw-alias-label-secondary);cursor:pointer;
  transition:background-color .1s,color .1s;
}
@media (hover:hover){.dshr-rail:hover:not(:disabled){background:var(--dsw-alias-interactive-bg-hover);color:var(--dsw-alias-label-primary)}}
.dshr-rail:disabled{opacity:.55;cursor:default}
.dshr-rail[data-busy="true"] .dshr-icon{animation:dshr-spin .9s linear infinite;transform-origin:50% 50%}
`

    function ensureStyle() {
      const existing = document.getElementById(STYLE_ID)
      // HMR 会重新执行 apply()：旧样式表还在，必须整表覆盖。
      // 只按 id 判重会让改过的 CSS 永远进不来（曾因此只渲染出裸文本）。
      if (existing !== null) {
        if (existing.textContent !== CSS) existing.textContent = CSS
        return
      }
      const style = document.createElement('style')
      style.id = STYLE_ID
      style.textContent = CSS
      document.head.appendChild(style)
    }

    const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms))

    async function requestRestart(trigger) {
      const response = await fetch('/dsh-restart/restart', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-dsh-restart': '1' },
        body: JSON.stringify({ trigger }),
      })
      const data = await response.json().catch(() => ({}))
      if (!response.ok || data.ok !== true) {
        throw new Error(data.error ?? `HTTP ${response.status}`)
      }
      return data
    }

    async function hostAlive() {
      try {
        const response = await fetch('/dsh-restart/state', { cache: 'no-store' })
        return response.ok
      } catch {
        return false
      }
    }

    /**
     * 等宿主重启完再刷新页面。
     *
     * 顺序很关键：必须先真的看到宿主「挂掉过一次」，才认后来那次成功。
     * 否则 POST 回来后的头几百毫秒宿主还活着，会被误判成「已经回来了」直接刷新。
     */
    async function reloadWhenBack(alive) {
      let seenDown = false
      for (let i = 0; i < POLL_LIMIT; i += 1) {
        await sleep(POLL_MS)
        if (!alive.current) return
        const up = await hostAlive()
        if (!up) {
          seenDown = true
          continue
        }
        if (seenDown) {
          location.reload()
          return
        }
      }
    }

    const ICON = h(
      'svg',
      {
        className: 'dshr-icon',
        viewBox: '0 0 16 16',
        fill: 'none',
        stroke: 'currentColor',
        strokeWidth: 1.7,
        strokeLinecap: 'round',
        strokeLinejoin: 'round',
        'aria-hidden': 'true',
      },
      h('path', { d: 'M13.4 6.4A5.6 5.6 0 1 0 13.6 9.7' }),
      h('path', { d: 'M13.2 2.6v3.9H9.3' }),
    )

    function RestartEntry(props) {
      const wide = props?.wide !== false
      /** idle → sending → requested，失败进 error（按钮变成「重试」）。 */
      const [phase, setPhase] = useState('idle')
      const [error, setError] = useState(null)
      const mounted = useRef(true)

      useEffect(() => {
        mounted.current = true
        return () => {
          mounted.current = false
        }
      }, [])


      const fire = useCallback(async () => {
        if (phase === 'sending' || phase === 'requested') return
        setPhase('sending')
        setError(null)
        try {
          await requestRestart('sidebar')
          if (!mounted.current) return
          setPhase('requested')
          void reloadWhenBack(mounted)
        } catch (failure) {
          if (!mounted.current) return
          setPhase('error')
          setError(String(failure?.message ?? failure))
        }
      }, [phase])

      const busy = phase === 'sending' || phase === 'requested'
      const actionLabel = busy ? '重启中…' : (phase === 'error' ? '重试' : '重启')
      const subtitle = error !== null ? `重启失败：${error}` : (busy ? '正在重启…' : '重启 DSH 服务')

      if (!wide) {
        return h(
          'button',
          {
            type: 'button',
            className: 'dshr-rail',
            onClick: fire,
            disabled: busy,
            title: HINT,
            'aria-label': `一键重启：${HINT}`,
            'data-busy': busy ? 'true' : 'false',
          },
          ICON,
        )
      }

      return h(
        'div',
        { className: 'dshr-card', title: HINT },
        h(
          'span',
          { className: 'dshr-text' },
          h('span', { className: 'dshr-title' }, '一键重启'),
          h('span', {
            className: 'dshr-sub',
            'data-tone': error === null ? undefined : 'error',
          }, subtitle),
        ),
        h(
          'button',
          {
            type: 'button',
            className: 'dshr-action',
            onClick: fire,
            disabled: busy,
            'data-busy': busy ? 'true' : 'false',
          },
          actionLabel,
        ),
      )
    }

    return {
      inject: ['slots'],
      apply(ctx) {
        ensureStyle()
        ctx.slots.inject('sidebar.footer.action', () => ctx.slots.register({
          name: 'sidebar.footer.action',
          id: 'dsh-restart',
          order: 50,
          label: () => '一键重启',
        }, RestartEntry))
      },
    }
  },
})
