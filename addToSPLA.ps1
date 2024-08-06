$groupname = Read-Host "Enter the name of the current RDS group: "
$users = Get-ADGroupMember -Identity $groupname | ? {$_.objectclass -eq "user"}
$samnames = New-Object System.Collections.Generic.List[System.Object]
foreach ($activeusers in $users) { Get-ADUser -Identity $activeusers | write-host( }

foreach ($user in $samnames) {Add-ADPrincipalGroupMembership -identity $user -memberof "SPLA RDS Users"}
