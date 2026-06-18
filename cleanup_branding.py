from pathlib import Path

root = Path('c:/Users/Admin/Desktop/Harusi')
files = [
    root / 'assets' / 'index-B9S4yvVQ.js',
    root / 'Let Glory Manifest' / 'assets' / 'index-B9S4yvVQ.js'
]

replacements = [
    (
        'E&&We.jsxs(JM,{value:"ai",children:[We.jsx($g,{className:"w-3 h-3 mr-1"}),"AI Assistant"]}),',
        ''
    ),
    (
        'E&&We.jsx(ZM,{value:"ai",children:We.jsx(sD,{password:YM.Dev})}),',
        ''
    ),
    (
        'fP="/__l5e/assets-v1/ffbaa7c6-ae14-4a47-99ee-fe6d451bbc4b/let-glory-manifest.png"',
        'fP="/assets/hero-mobile.png"'
    ),
    (
        'Powered by the local assistant.',
        ''
    ),
    (
        'Powered by Lovable AI. The assistant can edit live site copy directly — just ask. Changes go live instantly and are recorded in the audit log.',
        ''
    ),
    (
        'We.jsx("footer",{className:"py-12 text-center border-t border-border/30",children:We.jsxs("div",{className:"flex items-center justify-center gap-2 text-foreground/30 text-sm",children:[We.jsx("span",{children:"Made with"}),We.jsx(Tg,{className:"w-3 h-3 text-accent/50 fill-accent/50"}),We.jsx("span",{children:"for Micah & Damaris"})]})})',
        'We.jsx("footer",{className:"py-12 text-center border-t border-border/30"})'
    ),
    (
        'Dev AI Assistant',
        ''
    ),
    (
        'Dev Assistant',
        ''
    ),
    (
        'Lovable AI',
        ''
    ),
    (
        'https://uuimnouiyseutmmzuuih.supabase.co/functions/v1/dev-ai',
        ''
    ),
    (
        "Hi! I\\'m your . Ask me anything",
        ''
    ),
    (
        'edit the live website copy for you on the spot',
        ''
    ),
]

for file in files:
    text = file.read_text(encoding='utf-8')
    original = text
    for old, new in replacements:
        text = text.replace(old, new)
    if text != original:
        file.write_text(text, encoding='utf-8')
        print(f'updated {file}')
    else:
        print(f'no changes needed {file}')
