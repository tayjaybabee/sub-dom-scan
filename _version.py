app_name = 'SubDomScan'
version = f'{app_name}_1.0'
pre_release = True

if pre_release:
    import _pre_release
    version = f'{version}({_pre_release.version})'

print(version)
