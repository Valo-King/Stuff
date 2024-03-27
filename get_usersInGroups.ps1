$groupname = "INSERT GROUP NAME HERE"

$users = Get-ADGroupMember -Identity $groupname | ? {$_.objectclass -eq "user"}

foreach ($activeusers in $users) { Get-ADUser -Identity $activeusers | ? {$_.enabled -eq $true} | select Name, SamAccountName, UserPrincipalName, Enabled }