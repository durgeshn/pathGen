import os
import ConfigParser

from config import bdg_path_config as mainConfig


class pathGenerator(object):
    def __init__(self, projectName):
        self.project = projectName
        a = 'from config import bdg_path_config as mainConfig'
        # initConfigCmd = 'from config import {}_path_config as mainConfig'.format(self.project.lower())
        # eval(initConfigCmd)
        # eval('from config import bdg_path_config as mainConfig')

    def getAssetPath(self, baseAstType, assetType, assetName, dept, upVersion=False, pathType='shotServer',
                     app='Maya'):
        basePathType = pathType.replace('Server', '').replace('Local', '')
        if assetType in mainConfig.ASSET_TYPE:
            assetType = mainConfig.ASSET_TYPE.get('ASSET_TYPE', assetType)

        pathType = '{}AssetPath'.format(pathType)
        confDeptName = mainConfig.DEPT.get('DEPT', dept)

        confFileName = mainConfig.PATH.get('{}FileName'.format(basePathType), None)

        confFilePath = mainConfig.PATH.get(pathType, None)
        confFilePath = os.path.join(confFilePath, confFileName).replace('\\', '/')
        confFilePath = confFilePath.replace('$DEPT', confDeptName)
        confFilePath = confFilePath.replace('$ASSETNAME', assetName)
        confFilePath = confFilePath.replace('$ASSETTYPE', assetType)
        version_type = mainConfig.REPO.get('versiontype')
        i = 999
        finalPathFolder = confFilePath.replace('$VER', version_type % i)
        while not os.path.isfile(finalPathFolder):
            i -= 1
            finalPathFolder = confFilePath.replace('$VER', version_type % i)
            if i == 0:
                break
        if upVersion:
            i = i+ 1
        return confFilePath.replace('$VER', version_type % i)

    def run(self):
        pass


if __name__ == '__main__':
    path_brk = pathGenerator('BDG')
    print path_brk.getAssetPath(baseAstType='sequence', assetType='BDG105', assetName='050', dept='ani', pathType='movServer'), '==================='
    print path_brk.getAssetPath(baseAstType='sequence', assetType='BDG105', assetName='006', dept='ani',
                                upVersion=True)
