$groupname = "<CHANGEME>"
$users = Get-ADGroupMember -identity $groupname | ? {$_.objectclass -eq "user"}
foreach ($activeusers in $users) { get-aduser -identity $activeusers | ? {$_.enabled -eq $true} | select Name, SamAccountName, UserPrincipalName, Enabled }
