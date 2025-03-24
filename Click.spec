# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Saintsburg\\PycharmProjects\\Habit_Tracker1\\Click.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Saintsburg\\PycharmProjects\\Habit_Tracker1\\Database.py', '.'), ('C:\\Users\\Saintsburg\\PycharmProjects\\Habit_Tracker1\\Habits.db', '.'), ('C:\\Users\\Saintsburg\\PycharmProjects\\Habit_Tracker1\\main.py', '.'), ('C:\\Users\\Saintsburg\\PycharmProjects\\Habit_Tracker1\\Test.py', '.')],
    hiddenimports=['click', 'click._termui_impl', 'click_shell'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Click',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Click',
)
