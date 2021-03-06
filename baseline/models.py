from django.db import models


# Create your models here.
class AllScanResRecord(models.Model):
    scanTime=models.DateTimeField(verbose_name="scanTime")
    scanType=models.CharField(max_length=50,verbose_name="scanTime")
    hostname=models.CharField(max_length=100,verbose_name="hostname")
    osVersion=models.CharField(max_length=100,verbose_name="osVersion")
    ipList=models.CharField(max_length=100,verbose_name="ipList")
    macaddr=models.CharField(max_length=100,verbose_name="macaddr")
    def __str__(self):
        return '%s %s' %(self.scanTime,self.macaddr)
    class Meta:
        verbose_name="所有安全基线的扫描记录"
        verbose_name_plural="所有安全基线的扫描记录"
class WindowsCheckRes(models.Model):
    # basic_info
    scanTime=models.DateTimeField(verbose_name="scanTime")
    hostname=models.CharField(max_length=100,verbose_name="hostname")
    osVersion=models.CharField(max_length=100,verbose_name="osVersion")
    ipList=models.CharField(max_length=100,verbose_name="ipList")
    macaddr=models.CharField(max_length=100,verbose_name="macaddr")

    # account_check_res
    ## password_check_info
    passwordHistorySize=models.CharField(max_length=20,default="False",verbose_name="passwordHistorySize")
    maximumPasswordAge=models.CharField(max_length=20,default="False",verbose_name="maximumPasswordAge")
    minimumPasswordAge=models.CharField(max_length=20,default="False",verbose_name="minimumPasswordAge")
    passwordComplexity=models.CharField(max_length=20,default="False",verbose_name="passwordComplexity")
    clearTextPassword=models.CharField(max_length=20,default="False",verbose_name="clearTextPassword")
    minimumPasswordLength=models.CharField(max_length=20,default="False",verbose_name="minimumPasswordLength")
    ## account_lockout_info
    lockoutDuration=models.CharField(max_length=20,default="False",verbose_name="lockoutDuration")
    lockoutBadCount=models.CharField(max_length=20,default="False",verbose_name="lockoutBadCount")
    resetLockoutCount=models.CharField(max_length=20,default="False",verbose_name="resetLockoutCount")

    # audit_check_res
    auditPolicyChange=models.CharField(max_length=20,default="False",verbose_name="auditPolicyChange")
    auditLogonEvents=models.CharField(max_length=20,default="False",verbose_name="auditLogonEvents")
    auditObjectAccess=models.CharField(max_length=20,default="False",verbose_name="auditObjectAccess")
    auditProcessTracking=models.CharField(max_length=20,default="False",verbose_name="auditProcessTracking")
    auditDSAccess=models.CharField(max_length=20,default="False",verbose_name="auditDSAccess")
    auditSystemEvents=models.CharField(max_length=20,default="False",verbose_name="auditSystemEvents")
    auditAccountLogon=models.CharField(max_length=20,default="False",verbose_name="auditAccontLogon")
    auditAccountManage=models.CharField(max_length=20,default="False",verbose_name="auditAccountManage")

    # userright_check_res
    seTrustedCredManAccessPrivilegeIFNone=models.CharField(max_length=20,default="False",verbose_name="seTrustedCredManAccessPrivilegeIFNone")
    seTcbPrivilegeIFNone=models.CharField(max_length=20,default="False",verbose_name="seTcbPrivilegeIFNone")
    seMachineAccountPrivilegeIFOnlySpecifiedUserOrArray=models.CharField(max_length=20,default="False",verbose_name="seMachineAccountPrivilegeIFOnlySpecifiedUserOrArray")
    seCreateGlobalPrivilegeIFNone=models.CharField(max_length=20,default="False",verbose_name="seCreateGlobalPrivilegeIFNone")
    seDenyBatchLogonRightIFContainGuests=models.CharField(max_length=20,default="False",verbose_name="seDenyBatchLogonRightIFContainGuests")
    seDenyServiceLogonRightIFContainGuests=models.CharField(max_length=20,default="False",verbose_name="seDenyServiceLogonRightIFContainGuests")
    seDenyInteractiveLogonRightIFContainGuests=models.CharField(max_length=20,default="False",verbose_name="seDenyInteractiveLogonRightIFContainGuests")
    seRemoteShutdownPrivilegeIFOnlySpecifiedUserOrArray=models.CharField(max_length=20,default="False",verbose_name="seRemoteShutdownPrivilegeIFOnlySpecifiedUserOrArray")
    seRelabelPrivilegeIFNone=models.CharField(max_length=20,default="False",verbose_name="seRelabelPrivilegeIFNone")
    seSyncAgentPrivilegeIFNone=models.CharField(max_length=20,default="False",verbose_name="seSyncAgentPrivilegeIFNone")

    # secureoption_check_res
    enableGuestAccount=models.CharField(max_length=20,default="False",verbose_name="enableGuestAccount")
    limitBlankPasswordUse=models.CharField(max_length=20,default="False",verbose_name="limitBlankPasswordUse")
    newAdministratorName=models.CharField(max_length=20,default="False",verbose_name="newAdministratorName")
    newGuestName=models.CharField(max_length=20,default="False",verbose_name="newGuestName")
    dontDisplayLastUserName=models.CharField(max_length=20,default="False",verbose_name="dontDisplayLastUserName")
    disableCAD=models.CharField(max_length=20,default="False",verbose_name="disableCAD")
    inactivityTimeoutSecs=models.CharField(max_length=20,default="False",verbose_name="inactivityTimeoutSecs")
    enablePlainTextPassword=models.CharField(max_length=20,default="False",verbose_name="enablePlainTextPassword")
    autoDisconnect=models.CharField(max_length=20,default="False",verbose_name="autoDisconnect")
    noLMHash=models.CharField(max_length=20,default="False",verbose_name="noLMHash")
    lsaAnonymousNameLookup=models.CharField(max_length=20,default="False",verbose_name="lsaAnonymousNameLookup")
    restrictAnonymousSAM=models.CharField(max_length=20,default="False",verbose_name="restrictAnonymousSAM")
    restrictAnonymous=models.CharField(max_length=20,default="False",verbose_name="restrictAnonymous")
    clearPageFileAtShutdown=models.CharField(max_length=20,default="False",verbose_name="clearPageFileAtShutdown")

    # portsecure_check_res
    rdpPort=models.CharField(max_length=20,default="False",verbose_name="rdpPort")

    # systemsecure_check_res
    autoRunRes=models.CharField(max_length=20,default="False",verbose_name="autoRunRes")
    def __str__(self):
        return '%s %s'%(self.scanTime,self.macaddr)
    class Meta:
        verbose_name="Windows安全基线检查结果"
        verbose_name="windows安全基线检查结果"
class WindowsScanResMeta(models.Model):
    # 时间
    scanTime=models.DateTimeField(verbose_name="scanTime")
    # macaddr
    macaddr=models.CharField(max_length=100,verbose_name="macaddr")
    # 扫描结果
    windowsScanResMetaData=models.CharField(max_length=100000,verbose_name="windowsScanResMeta")
    def __str__(self):
        return '%s %s'%(self.scanTime,self.macaddr)
    class Meta:
        verbose_name="windows安全基线扫描结果元数据"
        verbose_name_plural="Windows安全基线扫描结果元数据"

class WindowsScanRes(models.Model):
    # basic_info
    scanTime=models.DateTimeField(verbose_name="scanTime")
    hostname=models.CharField(max_length=100,verbose_name="hostname")
    osVersion=models.CharField(max_length=100,verbose_name="osVersion")
    ipList=models.CharField(max_length=100,verbose_name="ipList")
    macaddr=models.CharField(max_length=100,verbose_name="macaddr")

    # account_check_res
    ## password_check_info
    passwordHistorySize=models.IntegerField(verbose_name="passwordHistorySize")
    maximumPasswordAge=models.IntegerField(verbose_name="maximumPasswordAge")
    minimumPasswordAge=models.IntegerField(verbose_name="minimumPasswordAge")
    passwordComplexity=models.IntegerField(verbose_name="passwordComplexity")
    clearTextPassword=models.IntegerField(verbose_name="clearTextPassword")
    minimumPasswordLength=models.IntegerField(verbose_name="minimumPasswordLength")
    ## account_lockout_info
    lockoutDuration=models.IntegerField(verbose_name="lockoutDuration")
    lockoutBadCount=models.IntegerField(verbose_name="lockoutBadCount")
    resetLockoutCount=models.IntegerField(verbose_name="resetLockoutCount")

    # audit_check_res
    auditPolicyChange=models.IntegerField(verbose_name="auditPolicyChange")
    auditLogonEvents=models.IntegerField(verbose_name="auditLogonEvents")
    auditObjectAccess=models.IntegerField(verbose_name="auditObjectAccess")
    auditProcessTracking=models.IntegerField(verbose_name="auditProcessTracking")
    auditDSAccess=models.IntegerField(verbose_name="auditDSAccess")
    auditSystemEvents=models.IntegerField(verbose_name="auditSystemEvents")
    auditAccountLogon=models.IntegerField(verbose_name="auditAccontLogon")
    auditAccountManage=models.IntegerField(verbose_name="auditAccountManage")

    # userright_check_res
    seTrustedCredManAccessPrivilegeIFNone=models.CharField(max_length=100,verbose_name="seTrustedCredManAccessPrivilegeIFNone")
    seTcbPrivilegeIFNone=models.CharField(max_length=100,verbose_name="seTcbPrivilegeIFNone")
    seMachineAccountPrivilegeIFOnlySpecifiedUserOrArray=models.CharField(max_length=100,verbose_name="seMachineAccountPrivilegeIFOnlySpecifiedUserOrArray")
    seCreateGlobalPrivilegeIFNone=models.CharField(max_length=100,verbose_name="seCreateGlobalPrivilegeIFNone")
    seDenyBatchLogonRightIFContainGuests=models.BooleanField(verbose_name="seDenyBatchLogonRightIFContainGuests")
    seDenyServiceLogonRightIFContainGuests=models.BooleanField(verbose_name="seDenyServiceLogonRightIFContainGuests")
    seDenyInteractiveLogonRightIFContainGuests=models.BooleanField(verbose_name="seDenyInteractiveLogonRightIFContainGuests")
    seRemoteShutdownPrivilegeIFOnlySpecifiedUserOrArray=models.CharField(max_length=100,verbose_name="seRemoteShutdownPrivilegeIFOnlySpecifiedUserOrArray")
    seRelabelPrivilegeIFNone=models.CharField(max_length=100,verbose_name="seRelabelPrivilegeIFNone")
    seSyncAgentPrivilegeIFNone=models.CharField(max_length=100,verbose_name="seSyncAgentPrivilegeIFNone")

    # secureoption_check_res
    enableGuestAccount=models.BooleanField(verbose_name="enableGuestAccount")
    limitBlankPasswordUse=models.BooleanField(verbose_name="limitBlankPasswordUse")
    newAdministratorName=models.BooleanField(verbose_name="newAdministratorName")
    newGuestName=models.BooleanField(verbose_name="newGuestName")
    dontDisplayLastUserName=models.BooleanField(verbose_name="dontDisplayLastUserName")
    disableCAD=models.BooleanField(verbose_name="disableCAD")
    inactivityTimeoutSecs=models.CharField(max_length=100,verbose_name="inactivityTimeoutSecs")
    enablePlainTextPassword=models.BooleanField(verbose_name="enablePlainTextPassword")
    autoDisconnect=models.CharField(max_length=100,verbose_name="autoDisconnect")
    noLMHash=models.BooleanField(verbose_name="noLMHash")
    lsaAnonymousNameLookup=models.BooleanField(verbose_name="lsaAnonymousNameLookup")
    restrictAnonymousSAM=models.BooleanField(verbose_name="restrictAnonymousSAM")
    restrictAnonymous=models.BooleanField(verbose_name="restrictAnonymous")
    clearPageFileAtShutdown=models.BooleanField(verbose_name="clearPageFileAtShutdown")

    # portsecure_check_res
    rdpPort=models.CharField(max_length=10,verbose_name="rdpPort")

    # systemsecure_check_res
    autoRunRes=models.CharField(max_length=10,verbose_name="autoRunRes")

    def __str__(self):
        return '%s %s'%(self.scanTime,self.macaddr)
    class Meta:
        verbose_name="windows安全基线扫描结果元数据"
        verbose_name_plural="Windows安全基线扫描结果元数据"

class LinuxScanResMeta(models.Model):
    # 时间
    scanTime=models.DateTimeField(verbose_name="scanTime")
    # macaddr
    macaddr=models.CharField(max_length=100,verbose_name="macaddr")
    # 扫描结果
    linuxScanResMetaData=models.CharField(max_length=100000,verbose_name="linuxScanResMeta")
    def __str__(self):
        return '%s %s'%(self.scanTime,self.macaddr)  #("LinuxScanResMeta")
    class Meta:
        verbose_name='Linux安全基线扫描结果元数据'
        verbose_name_plural='Linux安全基线扫描结果元数据'

class LinuxCheckRes(models.Model):
    # basic_info
    scanTime=models.DateTimeField(verbose_name="scanTime")
    hostname=models.CharField(max_length=100,verbose_name="hostname")
    osVersion=models.CharField(max_length=100,verbose_name="osVersion")
    ipList=models.CharField(max_length=100,verbose_name="ipList")
    macaddr=models.CharField(max_length=100,verbose_name="macaddr")
    kernelVersion=models.CharField(max_length=100,verbose_name="macaddr")
    # 
    ck_tmpIfSeparate=models.CharField(max_length=20,default="False",verbose_name="ck_tmpIfSeparate")
    ck_tmpIfNoexec=models.CharField(max_length=20,default="False",verbose_name="ck_tmpIfNoexec")
    ck_tmpIfNosuid=models.CharField(max_length=20,default="False",verbose_name="ck_tmpIfNosuid")
    ck_grubcfgPermissionLE600=models.CharField(max_length=20,default="False",verbose_name="ck_grubcfgPermissionLE600")
    ck_grubcfgIfSetPasswd=models.CharField(max_length=20,default="False",verbose_name="ck_grubcfgIfSetPasswd")
    ck_singleUserModeIfNeedAuth=models.CharField(max_length=20,default="False",verbose_name="ck_singleUserModeIfNeedAuth")
    ck_selinuxStateIfEnforcing=models.CharField(max_length=20,default="False",verbose_name="ck_selinuxStateIfEnforcing")
    ck_selinuxPolicyIfConfigured=models.CharField(max_length=20,default="False",verbose_name="ck_selinuxPolicyIfConfigured")
    ck_timeSyncServerIfConfigured=models.CharField(max_length=20,default="False",verbose_name="ck_timeSyncServerIfConfigured")
    ck_x11windowIfNotInstalled=models.CharField(max_length=20,default="False",verbose_name="ck_x11windowIfNotInstalled")
    ck_hostsAllowFilePermission=models.CharField(max_length=20,default="False",verbose_name="ck_hostsAllowFilePermission")
    ck_hostsAllowFileIfConfigured=models.CharField(max_length=20,default="False",verbose_name="ck_hostsAllowFileIfConfigured")
    ck_hostsDenyFilePermission=models.CharField(max_length=20,default="False",verbose_name="ck_hostsDenyFilePermission")
    ck_hostsDenyFileIfConfigured=models.CharField(max_length=20,default="False",verbose_name="ck_hostsDenyFileIfConfigured")
    ck_iptablesIfInstalled=models.CharField(max_length=20,default="False",verbose_name="ck_iptablesIfInstalled")
    ck_iptablesInputPolicyIfDrop=models.CharField(max_length=20,default="False",verbose_name="ck_iptablesInputPolicyIfDrop")
    ck_iptablesOutputPolicyIfDrop=models.CharField(max_length=20,default="False",verbose_name="ck_iptablesOutputPolicyIfDrop")
    ck_auditdIfEnabled=models.CharField(max_length=20,default="False",verbose_name="ck_auditdIfEnabled")
    ck_auditdIfSetMaxLogFile=models.CharField(max_length=20,default="False",verbose_name="ck_auditdIfSetMaxLogFile")
    ck_auditdIfSetMaxLogFileAction=models.CharField(max_length=20,default="False",verbose_name="ck_auditdIfSetMaxLogFileAction")
    ck_auditdIfSetSpaceLeftAction=models.CharField(max_length=20,default="False",verbose_name="ck_auditdIfSetSpaceLeftAction")
    ck_auditdIfSetNumLogs=models.CharField(max_length=20,default="False",verbose_name="ck_auditdIfSetNumLogs")
    ck_auditdIfCheckTimechange=models.CharField(max_length=20,default="False",verbose_name="ck_auditdIfCheckTimechange")
    ck_auditdRulesNotCheckedUserandgroupfile=models.CharField(max_length=20,default="False",verbose_name="ck_auditdRulesNotCheckedUserandgroupfile")
    ck_auditdRulesNotCheckedLoginoutEvents=models.CharField(max_length=20,default="False",verbose_name="ck_auditdRulesNotCheckedUserandgroupfileLoginoutEvents")
    ck_auditdRulesNotCheckedNetworkenv=models.CharField(max_length=20,default="False",verbose_name="ck_auditdRulesNotCheckedNetworkenv")
    ck_auditdRulesNotCheckedMACchange=models.CharField(max_length=20,default="False",verbose_name="ck_auditdRulesNotCheckedMACchange")
    ck_auditdRulesNotCheckedDACChangeSyscall=models.CharField(max_length=20,default="False",verbose_name="ck_auditdRulesNotCheckedDACChangeSyscall")
    ck_auditdRulesNotCheckedFileAccessAttemptSyscall=models.CharField(max_length=20,default="False",verbose_name="ck_auditdRulesNotCheckedFileAccessAttemptSyscall")
    ck_auditdRulesNotCheckedPrivilegedCommand=models.CharField(max_length=20,default="False",verbose_name="ck_auditdRulesNotCheckedPrivilegedCommand")
    ck_auditdRulesNotCheckedSudoerFile=models.CharField(max_length=20,default="False",verbose_name="ck_auditdRulesNotCheckedSudoerFile")
    ck_auditdRulesIfImmutable=models.CharField(max_length=20,default="False",verbose_name="ck_auditdRulesIfImmutable")
    ck_rsyslogIfEnabled=models.CharField(max_length=20,default="False",verbose_name="ck_rsyslogIfEnabled")
    ck_crondIfEnabled=models.CharField(max_length=20,default="False",verbose_name="ck_crondIfEnabled")
    ck_crondConfigFilePermissionArray=models.CharField(max_length=20,default="False",verbose_name="ck_crondConfigFilePermissionArray")
    ck_crondallowdenyFilePermissionArray=models.CharField(max_length=20,default="False",verbose_name="ck_crondallowdenyFilePermissionArray")
    ck_sshdConfigFilePermission=models.CharField(max_length=20,default="False",verbose_name="ck_sshdConfigFilePermission")
    ck_sshdIfDisableX11forwarding=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfDisableX11forwarding")
    ck_sshdIfSetMaxAuthTries=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfSetMaxAuthTries")
    ck_sshdIfEnableIgnoreRhosts=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfEnableIgnoreRhosts")
    ck_sshdIfDisableHostbasedAuthentication=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfDisableHostbasedAuthentication")
    ck_sshdIfDisablePermitRootLogin=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfDisablePermitRootLogin")
    ck_sshdIfDisablePermitEmptyPasswords=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfDisablePermitEmptyPasswords")
    ck_sshdIfDisablePermitUserEnvironment=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfDisablePermitUserEnvironment")
    ck_sshdIfSpecificMACs=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfSpecificMACs")
    ck_sshdIfSetClientAliveInterval=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfSetClientAliveInterval")
    ck_sshdIfSetLoginGraceTime=models.CharField(max_length=20,default="False",verbose_name="ck_sshdIfSetLoginGraceTime")
    ck_pamIfSetMinlen=models.CharField(max_length=20,default="False",verbose_name="ck_pamIfSetMinlen")
    ck_pamIfSetMinclass=models.CharField(max_length=20,default="False",verbose_name="ck_pamIfSetMinclass")
    ck_sshdNotSetedLockAndUnlockTimeFiles=models.CharField(max_length=20,default="False",verbose_name="ck_sshdNotSetedLockAndUnlockTimeFiles")
    ck_sshdPamdFileReuseLimitArray=models.CharField(max_length=20,default="False",verbose_name="ck_sshdPamdFileReuseLimitArray")
    ck_sshdPamdFileIfSetSha512Array=models.CharField(max_length=20,default="False",verbose_name="ck_sshdPamdFileIfSetSha512Array")
    ck_accountPassMaxDays=models.CharField(max_length=20,default="False",verbose_name="ck_accountPassMaxDays")
    ck_accountPassMinDays=models.CharField(max_length=20,default="False",verbose_name="ck_accountPassMinDays")
    ck_accountPassWarnDays=models.CharField(max_length=20,default="False",verbose_name="ck_accountPassWarnDays")
    ck_accountPassAutolockInactiveDays=models.CharField(max_length=20,default="False",verbose_name="ck_accountPassAutolockInactiveDays")
    ck_accountShouldUnloginArray=models.CharField(max_length=20,default="False",verbose_name="ck_accountShouldUnloginArray")
    ck_accountGIDOfRoot=models.CharField(max_length=20,default="False",verbose_name="ck_accountGIDOfRoot")
    ck_accountProfileTMOUTArray=models.CharField(max_length=20,default="False",verbose_name="ck_accountProfileTMOUTArray")
    ck_accountIfSetUsersCanAccessSuCommand=models.CharField(max_length=20,default="False",verbose_name="ck_accountIfSetUsersCanAccessSuCommand")
    ck_importantFilePermissionArray=models.CharField(max_length=20,default="False",verbose_name="ck_importantFilePermissionArray")
    ck_importantFileUidgidArray=models.CharField(max_length=20,default="False",verbose_name="ck_importantFileUidgidArray")
    ck_userIfSetPasswdOrArray=models.CharField(max_length=20,default="False",verbose_name="ck_userIfSetPasswdOrArray")
    ck_uid0OnlyRootOrArray=models.CharField(max_length=20,default="False",verbose_name="ck_uid0OnlyRootOrArray")
    ck_pathDirIfNotHasDot=models.CharField(max_length=20,default="False",verbose_name="ck_pathDirIfNotHasDot")
    ck_pathDirPermissionHasGWArray=models.CharField(max_length=20,default="False",verbose_name="ck_pathDirPermissionHasGWArray")
    ck_pathDirPermissionHasOWArray=models.CharField(max_length=20,default="False",verbose_name="ck_pathDirPermissionHasOWArray")
    ck_pathDirDoesNotExistOrNotDirArray=models.CharField(max_length=20,default="False",verbose_name="ck_pathDirDoesNotExistOrNotDirArray")
    ck_userHomeDirIfExistArray=models.CharField(max_length=20,default="False",verbose_name="ck_userHomeDirIfExistArray")
    ck_userHomeDirPermissionArray=models.CharField(max_length=20,default="False",verbose_name="ck_userHomeDirPermissionArray")
    ck_userIfOwnTheirHomeDirArray=models.CharField(max_length=20,default="False",verbose_name="ck_userIfOwnTheirHomeDirArray")
    ck_userHomeDirIfHasGWorOWDotFileArray=models.CharField(max_length=20,default="False",verbose_name="ck_userHomeDirIfHasGWorOWDotFileArray")
    ck_userHomeDirIfHasOtherFileArray=models.CharField(max_length=20,default="False",verbose_name="ck_userHomeDirIfHasOtherFileArray")
    ck_groupNotExistInetcgroup=models.CharField(max_length=20,default="False",verbose_name="ck_groupNotExistInetcgroup")
    ck_usersIfHasUniqueUIDArray=models.CharField(max_length=20,default="False",verbose_name="ck_usersIfHasUniqueUIDArray")
    ck_groupsIfHasUniqueGIDArray=models.CharField(max_length=20,default="False",verbose_name="ck_groupsIfHasUniqueGIDArray")

    def __str__(self):
        return '%s %s' %(self.scanTime,self.macaddr)
    class Meta:
        verbose_name="Linux安全基线检查结果"
        verbose_name_plural="Linux安全基线检查结果"

class LinuxScanRes(models.Model):
    scanTime=models.DateTimeField(verbose_name="scanTime")
    # basic_info
    #publicIP=models.CharField(max_length=30,verbose_name="publicIP")
    #privateIP=models.CharField(max_length=30,verbose_name="privateIP")
    ipList=models.CharField(max_length=100,verbose_name="ipList")
    hostname=models.CharField(max_length=100,verbose_name="hostname")
    macaddr=models.CharField(max_length=100,verbose_name="macaddr")
    osVersion=models.CharField(max_length=30,verbose_name="osVersion")
    kernelVersion=models.CharField(max_length=30,verbose_name="kernelVersion")

    # init_check_res
    ## tmp_partition_info
    #tmpIfSeparate=models.BooleanField(default=False, verbose_name="tmpIfSeparate")
    tmpIfSeparate=models.CharField(max_length=10,verbose_name="tmpIfSeparate")
    #tmpIfNoexec=models.BooleanField(default=False,verbose_name="tmpIfNoexec")
    tmpIfNoexec=models.CharField(max_length=10,verbose_name="tmpIfNoexec")
    #tmpIfNosuid=models.BooleanField(default=False,verbose_name="tmpIfNosuid")
    tmpIfNosuid=models.CharField(max_length=10,verbose_name="tmpIfNosuid")
    ## boot_secure_info
    #grubcfgIfExist=models.BooleanField(default=True,verbose_name="grubcfgIfExist")
    grubcfgIfExist=models.CharField(max_length=10,verbose_name="grubcfgIfExist")
    #grubcfgPermission=models.CharField(max_length=5,verbose_name="grubcfgPermission")
    grubcfgPermission=models.CharField(max_length=10,verbose_name="grubcfgPermission")
    #grubcfgIfSetPasswd=models.BooleanField(default=False,verbose_name="grubcfgIfSetPasswd")
    grubcfgIfSetPasswd=models.CharField(max_length=10,verbose_name="grubcfgIfSetPasswd")
    #singleUserModeIfNeedAuth=models.BooleanField(default=False,verbose_name="singleUserModeIfNeedAuth")
    singleUserModeIfNeedAuth=models.CharField(max_length=10,verbose_name="singleUserModeIfNeedAuth")
    #selinuxStateIfEnforcing=models.BooleanField(default=True,verbose_name="selinuxStateIfEnforcing")
    selinuxStateIfEnforcing=models.CharField(max_length=10,verbose_name="selinuxStateIfEnforcing")
    #selinuxPolicyIfConfigured=models.BooleanField(default=True,verbose_name="selinuxPolicyIfConfigured")
    selinuxPolicyIfConfigured=models.CharField(max_length=10,verbose_name="selinuxPolicyIfConfigured")

    # service_check_res
    #timeSyncServerIfConfigured=models.BooleanField(default=True,verbose_name="timeSyncServerIfConfigured")
    timeSyncServerIfConfigured=models.CharField(max_length=10,verbose_name="timeSyncServerIfConfigured")
    #x11windowIfNotInstalled=models.BooleanField(default=False,verbose_name="x11windowIfNotInstalled")
    x11windowIfNotInstalled=models.CharField(max_length=10,verbose_name="x11windowIfNotInstalled")

    # network_check_res
    #hostsAllowFileIfExist=models.BooleanField(default=True,verbose_name="hostsAllowFileIfExist")
    hostsAllowFileIfExist=models.CharField(max_length=10,verbose_name="hostsAllowFileIfExist")
    #hostsAllowFilePermission=models.CharField(max_length=5,verbose_name="hostsAllowFilePermission")
    hostsAllowFilePermission=models.CharField(max_length=10,verbose_name="hostsAllowFilePermission")
    #hostsAllowFileIfConfigured=models.BooleanField(default=False,verbose_name="hostsAllowFileIfConfigured")
    hostsAllowFileIfConfigured=models.CharField(max_length=10,verbose_name="hostsAllowFileIfConfigured")
    #hostsDenyFileIfExist=models.BooleanField(default=True,verbose_name="hostsDenyFileIfExist")
    hostsDenyFileIfExist=models.CharField(max_length=10,verbose_name="hostsDenyFileIfExist")
    #hostsDenyFilePermission=models.CharField(max_length=5,verbose_name="hostsDenyFilePermission")
    hostsDenyFilePermission=models.CharField(max_length=10,verbose_name="hostsDenyFilePermission")
    #hostsDenyFileIfConfigured=models.BooleanField(default=False,verbose_name="hostsDenyFileIfConfigured")
    hostsDenyFileIfConfigured=models.CharField(max_length=10,verbose_name="hostsDenyFileIfConfigured")
    #iptablesIfInstalled=models.BooleanField(default=True,verbose_name="iptablesIfInstalled")
    iptablesIfInstalled=models.CharField(max_length=10,verbose_name="iptablesIfInstalled")
    #iptablesInputPolicyIfDrop=models.BooleanField(default=False,verbose_name="iptablesInputPolicyIfDrop")
    iptablesInputPolicyIfDrop=models.CharField(max_length=10,verbose_name="iptablesInputPolicyIfDrop")
    #iptablesOutputPolicyIfDrop=models.BooleanField(default=False,verbose_name="iptablesOutputPolicyIfDrop")
    iptablesOutputPolicyIfDrop=models.CharField(max_length=10,verbose_name="iptablesOutputPolicyIfDrop")

    # auditd_check_res
    ## auditd_config_info
    #auditdIfEnabled=models.BooleanField(default=True,verbose_name="auditdIfEnabled")
    auditdIfEnabled=models.CharField(max_length=10,verbose_name="auditdIfEnabled")
    #auditdconfIfExist=models.BooleanField(default=True,verbose_name="aditdconfIfExist")
    auditdconfIfExist=models.CharField(max_length=10,verbose_name="aditdconfIfExist")
    #auditdIfSetMaxLogFile=models.CharField(max_length=5,verbose_name="auditdIfSetMaxLogFile")
    auditdIfSetMaxLogFile=models.CharField(max_length=10,verbose_name="auditdIfSetMaxLogFile")
    #auditdIfSetMaxLogFileAction=models.CharField(max_length=10,verbose_name="auditdIfSetMaxLogFileAction")
    auditdIfSetMaxLogFileAction=models.CharField(max_length=10,verbose_name="auditdIfSetMaxLogFileAction")
    #auditdIfSetSpaceLeftAction=models.CharField(max_length=10,verbose_name="auditdIfSetSpaceLeftAction")
    auditdIfSetSpaceLeftAction=models.CharField(max_length=10,verbose_name="auditdIfSetSpaceLeftAction")
    #auditdIfSetNumLogs=models.CharField(max_length=5,verbose_name="auditdIfSetNumLogs")
    auditdIfSetNumLogs=models.CharField(max_length=10,verbose_name="auditdIfSetNumLogs")
    ## auditd_rules_info
    #auditdRulesIfExist=models.BooleanField(default=True,verbose_name="auditdRulesIfExist")
    auditdRulesIfExist=models.CharField(max_length=10,verbose_name="auditdRulesIfExist")
    #auditdRulesIfNotNull=models.BooleanField(default=True,verbose_name="auditdRulesIfNotNull")
    auditdRulesIfNotNull=models.CharField(max_length=10,verbose_name="auditdRulesIfNotNull")
    #auditdIfCheckTimechange=models.BooleanField(default=False,verbose_name="auditdIfCheckTimechange")
    auditdIfCheckTimechange=models.CharField(max_length=10,verbose_name="auditdIfCheckTimechange")
    #auditdRulesCheckedUserandgroupfile=models.CharField(max_length=600,verbose_name="auditdRulesCheckUserandgroupfile")
    auditdRulesCheckedUserandgroupfile=models.CharField(max_length=10,verbose_name="auditdRulesCheckUserandgroupfile")
    #auditdRulesNotCheckedUserandgroupfile=models.CharField(max_length=600,verbose_name="auditdRulesNotCheckUserandgroupfile")
    auditdRulesNotCheckedUserandgroupfile=models.CharField(max_length=10,verbose_name="auditdRulesNotCheckUserandgroupfile")
    #auditdRulesCheckedNetworkenv=models.CharField(max_length=600,verbose_name="auditdRulesCheckedNetworkenv")
    auditdRulesCheckedNetworkenv=models.CharField(max_length=10,verbose_name="auditdRulesCheckedNetworkenv")
    #auditdRulesNotCheckedNetworkenv=models.CharField(max_length=600,verbose_name="auditdRulesNotCheckedNetworkenv")
    auditdRulesNotCheckedNetworkenv=models.CharField(max_length=10,verbose_name="auditdRulesNotCheckedNetworkenv")
    #auditdRulesCheckedMACchange=models.CharField(max_length=600,verbose_name="auditdRulesCheckedMACchange")
    auditdRulesCheckedMACchange=models.CharField(max_length=10,verbose_name="auditdRulesCheckedMACchange")
    #auditdRulesNotCheckedMACchange=models.CharField(max_length=600,verbose_name="auditdRulesNotCheckedMACchange")
    auditdRulesNotCheckedMACchange=models.CharField(max_length=10,verbose_name="auditdRulesNotCheckedMACchange")
    #auditdRulesCheckedLoginoutEvents=models.CharField(max_length=600,verbose_name="auditdRulesCheckedLoginoutEvents")
    auditdRulesCheckedLoginoutEvents=models.CharField(max_length=10,verbose_name="auditdRulesCheckedLoginoutEvents")
    #auditdRulesNotCheckedLoginoutEvents=models.CharField(max_length=600,verbose_name="auditdRulesNotCheckedLoginoutEvents")
    auditdRulesNotCheckedLoginoutEvents=models.CharField(max_length=10,verbose_name="auditdRulesNotCheckedLoginoutEvents")
    #auditdRulesCheckedDACChangeSyscall=models.CharField(max_length=600,verbose_name="auditdRulesCheckedDACChangeSyscall")
    auditdRulesCheckedDACChangeSyscall=models.CharField(max_length=10,verbose_name="auditdRulesCheckedDACChangeSyscall")
    #auditdRulesNotCheckedDACChangeSyscall=models.CharField(max_length=600,verbose_name="auditdRulesNotCheckedDACChangeSyscall")
    auditdRulesNotCheckedDACChangeSyscall=models.CharField(max_length=10,verbose_name="auditdRulesNotCheckedDACChangeSyscall")
    #auditdRulesCheckedFileAccessAttemptSyscall=models.CharField(max_length=600,verbose_name="auditdRulesCheckedFileAccessAttemptSyscall")
    auditdRulesCheckedFileAccessAttemptSyscall=models.CharField(max_length=10,verbose_name="auditdRulesCheckedFileAccessAttemptSyscall")
    #auditdRulesNotCheckedFileAccessAttemptSyscall=models.CharField(max_length=600,verbose_name="auditdRulesNotCheckedFileAccessAttemptSyscall")
    auditdRulesNotCheckedFileAccessAttemptSyscall=models.CharField(max_length=10,verbose_name="auditdRulesNotCheckedFileAccessAttemptSyscall")
    #auditdRulesCheckedPrivilegedCommand=models.CharField(max_length=600,verbose_name="auditdRulesCheckedPrivilegedCommand")
    auditdRulesCheckedPrivilegedCommand=models.CharField(max_length=10,verbose_name="auditdRulesCheckedPrivilegedCommand")
    #auditdRulesNotCheckedPrivilegedCommand=models.CharField(max_length=600,verbose_name="auditdRulesNotCheckedPrivilegedCommand")
    auditdRulesNotCheckedPrivilegedCommand=models.CharField(max_length=10,verbose_name="auditdRulesNotCheckedPrivilegedCommand")
    #auditdRulesCheckedSudoerFile=models.CharField(max_length=600,verbose_name="auditdRulesCheckedSudoerFile")
    auditdRulesCheckedSudoerFile=models.CharField(max_length=10,verbose_name="auditdRulesCheckedSudoerFile")
    #auditdRulesNotCheckedSudoerFile=models.CharField(max_length=600,verbose_name="auditdRulesNotCheckedSudoerFile")
    auditdRulesNotCheckedSudoerFile=models.CharField(max_length=10,verbose_name="auditdRulesNotCheckedSudoerFile")
    #auditdRulesIfImmutable=models.BooleanField(default=False,verbose_name="auditdRulesIfImmutable")
    auditdRulesIfImmutable=models.CharField(max_length=10,verbose_name="auditdRulesIfImmutable")

    # log_check_res
    #rsyslogIfEnabled=models.BooleanField(default=True,verbose_name="rsyslogIfEnabled")
    rsyslogIfEnabled=models.CharField(max_length=10,verbose_name="rsyslogIfEnabled")

    # authentication_check_res
    ## crond_config_info
    #crondIfEnabled=models.BooleanField(default=True,verbose_name="crondIfEnabled")
    crondIfEnabled=models.CharField(max_length=10,verbose_name="crondIfEnabled")
    #crondConfigFilenameArray=models.CharField(max_length=600,verbose_name="crondConfigFilenameArray")
    crondConfigFilenameArray=models.CharField(max_length=10,verbose_name="crondConfigFilenameArray")
    #crondConfigFilePermissionArray=models.CharField(max_length=600,verbose_name="crondConfigFilePermissionArray")
    crondConfigFilePermissionArray=models.CharField(max_length=10,verbose_name="crondConfigFilePermissionArray")
    #crondallowdenyFilenameArray=models.CharField(max_length=600,verbose_name="crondallowdenyFilenameArray")
    crondallowdenyFilenameArray=models.CharField(max_length=10,verbose_name="crondallowdenyFilenameArray")
    #crondallowdenyFileIfExistArray=models.CharField(max_length=600,verbose_name="crondallowdenyFileIfExist")
    crondallowdenyFileIfExistArray=models.CharField(max_length=10,verbose_name="crondallowdenyFileIfExist")
    #crondallowdenyFilePermissionArray=models.CharField(max_length=600,verbose_name="crondallowdenyFilePermissionArray")
    crondallowdenyFilePermissionArray=models.CharField(max_length=10,verbose_name="crondallowdenyFilePermissionArray")
    #crondallowdenyFileOwnerArray=models.CharField(max_length=600,verbose_name="crondallowdenyFileOwnerArray")
    crondallowdenyFileOwnerArray=models.CharField(max_length=10,verbose_name="crondallowdenyFileOwnerArray")
    ## sshd_config_info
    #sshdIfEnabled=models.BooleanField(default=True,verbose_name="sshdIfEnabled")
    sshdIfEnabled=models.CharField(max_length=10,verbose_name="sshdIfEnabled")
    #sshdConfigFilePermission=models.CharField(max_length=5,verbose_name="sshdConfigFilePermission")
    sshdConfigFilePermission=models.CharField(max_length=10,verbose_name="sshdConfigFilePermission")
    #sshdIfDisableX11forwarding=models.BooleanField(default=False,verbose_name="sshdIfDisableX11forwarding")
    sshdIfDisableX11forwarding=models.CharField(max_length=10,verbose_name="sshdIfDisableX11forwarding")
    #sshdIfSetMaxAuthTries=models.CharField(max_length=5 ,verbose_name="sshdIfSetMaxAuthTries")
    sshdIfSetMaxAuthTries=models.CharField(max_length=10,verbose_name="sshdIfSetMaxAuthTries")
    #sshdIfEnableIgnoreRhosts=models.BooleanField(default=False,verbose_name="sshdIfEnableIgnoreRhosts")
    sshdIfEnableIgnoreRhosts=models.CharField(max_length=10,verbose_name="sshdIfEnableIgnoreRhosts")
    #sshdIfDisableHostbasedAuthentication=models.BooleanField(default=False,verbose_name="sshdIfDisableHostbasedAuthentication")
    sshdIfDisableHostbasedAuthentication=models.CharField(max_length=10,verbose_name="sshdIfDisableHostbasedAuthentication")
    #sshdIfDisablePermitRootLogin=models.BooleanField(default=False,verbose_name="sshdIfDisablePermitRootLogin")
    sshdIfDisablePermitRootLogin=models.CharField(max_length=10,verbose_name="sshdIfDisablePermitRootLogin")
    #sshdIfDisablePermitEmptyPasswords=models.BooleanField(default=False,verbose_name="sshdIfDisablePermitEmptyPasswords")
    sshdIfDisablePermitEmptyPasswords=models.CharField(max_length=10,verbose_name="sshdIfDisablePermitEmptyPasswords")
    #sshdIfDisablePermitUserEnvironment=models.BooleanField(default=False,verbose_name="sshdIfDisablePermitUserEnvironment")
    sshdIfDisablePermitUserEnvironment=models.CharField(max_length=10,verbose_name="sshdIfDisablePermitUserEnvironment")
    #sshdIfSpecificMACs=models.BooleanField(default=False,verbose_name="sshdIfSpecificMACs")
    sshdIfSpecificMACs=models.CharField(max_length=10,verbose_name="sshdIfSpecificMACs")
    #sshdIfSetClientAliveInterval=models.BooleanField(default=False,verbose_name="sshdIfSetClientAliveInterval")
    sshdIfSetClientAliveInterval=models.CharField(max_length=10,verbose_name="sshdIfSetClientAliveInterval")
    #sshdIfSetLoginGraceTime=models.BooleanField(default=False,verbose_name="sshdIfSetLoginGraceTime")
    sshdIfSetLoginGraceTime=models.CharField(max_length=10,verbose_name="sshdIfSetLoginGraceTime")
    ## pam_config
    #pamPwqualityconfIfExist=models.BooleanField(default=False,verbose_name="pamPwqualityconfIfExist")
    pamPwqualityconfIfExist=models.CharField(max_length=10,verbose_name="pamPwqualityconfIfExist")
    #pamIfSetMinlen=models.CharField(max_length=6,verbose_name="pamIfSetMinlen")
    pamIfSetMinlen=models.CharField(max_length=10,verbose_name="pamIfSetMinlen")
    #pamIfSetMinclass=models.CharField(max_length=6,verbose_name="pamIfSetMinclass")
    pamIfSetMinclass=models.CharField(max_length=10,verbose_name="pamIfSetMinclass")
    #sshdSetedLockAndUnlockTimeFiles=models.CharField(max_length=600,verbose_name="sshdSetedLockAndUnlockTimeFiles")
    sshdSetedLockAndUnlockTimeFiles=models.CharField(max_length=10,verbose_name="sshdSetedLockAndUnlockTimeFiles")
    #sshdNotSetedLockAndUnlockTimeFiles=models.CharField(max_length=600,verbose_name="sshdNotSetedLockAndUnlockTimeFiles")
    sshdNotSetedLockAndUnlockTimeFiles=models.CharField(max_length=10,verbose_name="sshdNotSetedLockAndUnlockTimeFiles")
    #sshdPamdFileArray=models.CharField(max_length=600,verbose_name="sshdPamdFileArray")
    sshdPamdFileArray=models.CharField(max_length=10,verbose_name="sshdPamdFileArray")
    #sshdPamdFileReuseLimitArray=models.CharField(max_length=600,verbose_name="sshdPamdFileReuseLimitArray")
    sshdPamdFileReuseLimitArray=models.CharField(max_length=10,verbose_name="sshdPamdFileReuseLimitArray")
    #sshdPamdFileIfSetSha512Array=models.CharField(max_length=600,verbose_name="sshdPamdFileIfSetSha512Array")
    sshdPamdFileIfSetSha512Array=models.CharField(max_length=10,verbose_name="sshdPamdFileIfSetSha512Array")
    ## account_config_info
    #accountPassMaxDays=models.CharField(max_length=6,verbose_name="accountPassMaxDays")
    accountPassMaxDays=models.CharField(max_length=10,verbose_name="accountPassMaxDays")
    #accountPassMinDays=models.CharField(max_length=6,verbose_name="accountPassMinDays")
    accountPassMinDays=models.CharField(max_length=10,verbose_name="accountPassMinDays")
    #accountPassWarnDays=models.CharField(max_length=6,verbose_name="accountPassWarnDays")
    accountPassWarnDays=models.CharField(max_length=10,verbose_name="accountPassWarnDays")
    #accountPassAutolockInactiveDays=models.CharField(max_length=6,verbose_name="accountPassAutolockInactinveDays")
    accountPassAutolockInactiveDays=models.CharField(max_length=10,verbose_name="accountPassAutolockInactinveDays")
    #accountShouldUnloginArray=models.CharField(max_length=600,verbose_name="accountShouldUnloginArray")
    accountShouldUnloginArray=models.CharField(max_length=10,verbose_name="accountShouldUnloginArray")
    #accountGIDOfRoot=models.CharField(max_length=6,verbose_name="accountGIDOfRoot")
    accountGIDOfRoot=models.CharField(max_length=10,verbose_name="accountGIDOfRoot")
    #accountProfileFileArray=models.CharField(max_length=600,verbose_name="accountProfileFileArray")
    accountProfileFileArray=models.CharField(max_length=10,verbose_name="accountProfileFileArray")
    #accountProfileTMOUTArray=models.CharField(max_length=600,verbose_name="accountProfileTMOUTArray")
    accountProfileTMOUTArray=models.CharField(max_length=10,verbose_name="accountProfileTMOUTArray")
    #accountIfSetUsersCanAccessSuCommand=models.CharField(max_length=600,verbose_name="accountIfSetUsersCanAccessSuCommand")
    accountIfSetUsersCanAccessSuCommand=models.CharField(max_length=10,verbose_name="accountIfSetUsersCanAccessSuCommand")

    # system_check_res
    ## file_permission_info
    #importantFilenameArray=models.CharField(max_length=600,verbose_name="importantFilenameArray")
    importantFilenameArray=models.CharField(max_length=10,verbose_name="importantFilenameArray")
    #importantFilePermissionArray=models.CharField(max_length=300,verbose_name="importantFilePermissionArray")
    importantFilePermissionArray=models.CharField(max_length=10,verbose_name="importantFilePermissionArray")
    #importantFileUidgidArray=models.CharField(max_length=300,verbose_name="importantFileUidgidArray")
    importantFileUidgidArray=models.CharField(max_length=10,verbose_name="importantFileUidgidArray")
    ## usergroup_config_info
    #userIfSetPasswdOrArray=models.CharField(max_length=300,verbose_name="userIfSetPasswdOrArray")
    userIfSetPasswdOrArray=models.CharField(max_length=10,verbose_name="userIfSetPasswdOrArray")
    #uid0OnlyRootOrArray=models.CharField(max_length=300,verbose_name="uid0OnlyRootOrArray")
    uid0OnlyRootOrArray=models.CharField(max_length=10,verbose_name="uid0OnlyRootOrArray")
    #pathDirIfNotHasDot=models.CharField(max_length=600,verbose_name="pathDirIfNotHasDot")
    pathDirIfNotHasDot=models.CharField(max_length=10,verbose_name="pathDirIfNotHasDot")
    #pathDirPermissionHasGWArray=models.CharField(max_length=600,verbose_name="pathDirPermissionHasGWArray")
    pathDirPermissionHasGWArray=models.CharField(max_length=10,verbose_name="pathDirPermissionHasGWArray")
    #pathDirPermissionHasOWArray=models.CharField(max_length=600,verbose_name="pathDirPermissionHasOWArray")
    pathDirPermissionHasOWArray=models.CharField(max_length=10,verbose_name="pathDirPermissionHasOWArray")
    #pathDirOwnerIsNotRootArray=models.CharField(max_length=600,verbose_name="pathDirOwnerIsNotRootArray")
    pathDirOwnerIsNotRootArray=models.CharField(max_length=10,verbose_name="pathDirOwnerIsNotRootArray")
    #pathDirDoesNotExistOrNotDirArray=models.CharField(max_length=600,verbose_name="pathDirDoesNotExistOrNotDirArray")
    pathDirDoesNotExistOrNotDirArray=models.CharField(max_length=10,verbose_name="pathDirDoesNotExistOrNotDirArray")
    #userArray=models.CharField(max_length=300,verbose_name="userArray")
    userArray=models.CharField(max_length=10,verbose_name="userArray")
    #userHomeDirIfExistArray=models.CharField(max_length=600,verbose_name="userHomeDirIfExistArray")
    userHomeDirIfExistArray=models.CharField(max_length=10,verbose_name="userHomeDirIfExistArray")
    #userHomeDirPermissionArray=models.CharField(max_length=600,verbose_name="userHomeDirPermissionArray")
    userHomeDirPermissionArray=models.CharField(max_length=10,verbose_name="userHomeDirPermissionArray")
    #userIfOwnTheirHomeDirArray=models.CharField(max_length=300,verbose_name="userIfOwnTheirHomeDirArray")
    userIfOwnTheirHomeDirArray=models.CharField(max_length=10,verbose_name="userIfOwnTheirHomeDirArray")
    #userHomeDirIfHasGWorOWDotFileArray=models.CharField(max_length=600,verbose_name="userHomeDirIfHasGWorOWDotFileArray")
    userHomeDirIfHasGWorOWDotFileArray=models.CharField(max_length=10,verbose_name="userHomeDirIfHasGWorOWDotFileArray")
    #userHomeDirIfHasOtherFileArray=models.CharField(max_length=600,verbose_name="userHomeDirIfHasOtherFileArray")
    userHomeDirIfHasOtherFileArray=models.CharField(max_length=10,verbose_name="userHomeDirIfHasOtherFileArray")
    #groupNotExistInetcgroup=models.CharField(max_length=300,verbose_name="groupNotExistInetcgroup")
    groupNotExistInetcgroup=models.CharField(max_length=10,verbose_name="groupNotExistInetcgroup")
    #usersIfHasUniqueUIDArray=models.CharField(max_length=300,verbose_name="userIfHasUniqueUIDArray")
    usersIfHasUniqueUIDArray=models.CharField(max_length=10,verbose_name="userIfHasUniqueUIDArray")
    #groupsIfHasUniqueGIDArray=models.CharField(max_length=300,verbose_name="groupsIfHasUniqueGIDArray")
    groupsIfHasUniqueGIDArray=models.CharField(max_length=10,verbose_name="groupsIfHasUniqueGIDArray")

    def __str__(self):
        return '%s %s' % (self.scanTime,self.macaddr) #"LinuxScanResult"
    class Meta:
        verbose_name = "Linux安全基线扫描结果数据"
        verbose_name_plural = "Linux安全基线扫描结果数据"