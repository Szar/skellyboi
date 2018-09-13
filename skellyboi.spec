# -*- mode: python -*-

block_cipher = None


a = Analysis(['skellyboi.py'],
             pathex=['C:\\Users\\Butts\\Desktop\\skellyboi'],
             binaries=[],
             datas=[('C:\\Users\\Butts\\Desktop\\skellyboi\\templates', './templates'), ('C:\\Users\\Butts\\Desktop\\skellyboi\\static', './static')],
             hiddenimports=['dns','dns.dnssec','dns.e164','dns.namedict','dns.tsigkeyring','dns.update','dns.version','dns.wiredata','dns.zone','dns.message','email.mime.message','email.mime.multipart','email.mime.nonmultipart','email.mime.image','email.mime.text','email.mime.audio','email.mime.base','engineio.async_threading','engineio.async_eventlet','engineio.async_gevent', 'gevent.__hub_local', 'gevent', 'gevent.__greenlet_primitives', 'gevent.__compat','gevent.__config','gevent.__fileobjectcommon','gevent.__fileobjectposix','gevent.__greenlet_primitives','gevent.__hub_local','gevent.__hub_primitives','gevent.__ident','gevent.__imap','gevent.__interfaces','gevent.__monitor','gevent.__patcher','gevent.__semaphore','gevent.__socket2','gevent.__socket3','gevent.__socketcommon','gevent.__ssl2','gevent.__ssl3','gevent.__sslgte279','gevent.__tblib','gevent.__threading','gevent.__tracer','gevent.__util','gevent.__util_py2','gevent.__waiter','gevent._greenlet'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='skellyboi',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='skellyboi.ico')
