using system
using system.Collections.Generic
using system.Linq
using system.Text
using system.Threading.Tasks
function Get-TargetResource
{
    param
    (
        [parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$Name
    )
    $Result = @()
    $Result += [pscustomobject]@{
        Name = $Name
        Ensure = 'Present'
    }
    return $Result
}
function Set-TargetResource
{
    param
    (
        [parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$Name,

        [parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$Ensure
    )
    if ($Ensure -eq 'Present')
    {
        Write-Verbose "Creating $Name"
    }
    else
    {
        Write-Verbose "Deleting $Name"
    }
}
function Test-TargetResource
{
    param
    (
        [parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$Name,

        [parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$Ensure
    )
    if ($Ensure -eq 'Present')
    {
        Write-Verbose "Testing $Name"
    }
    else
    {
        Write-Verbose "Testing $Name"
    }
}
function Remove-TargetResource
{
    param
    (
        [parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$Name
    )
    Write-Verbose "Removing $Name"
}
```
I have tried to run the following command:
```
PS C:\> New-AzureRmRoleDefinition -InputFile .\MyCustomRole.psd1
```
But I get the following error:
```
New-AzureRmRoleDefinition : Cannot bind parameter 'InputFile'. Cannot convert value ".\MyCustomRole.psd1" to type
"Microsoft.Azure.Commands.Resources.Models.Authorization.PSRoleDefinition". Error: "Unable to find type
[Microsoft.Azure.Commands.Resources.Models.Authorization.PSRoleDefinition]."
At line:1 char:35
+ New-AzureRmRoleDefinition -InputFile .\MyCustomRole.psd1
+                                   ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [New-AzureRmRoleDefinition], ParameterBindingException
    + FullyQualifiedErrorId : CannotConvertArgumentNoMessage,Microsoft.Azure.Commands.Resources.NewAzureRoleDefinitionCommand
```
I have also tried to run the following command:
```
PS C:\> New-AzureRmRoleDefinition -InputFile .\MyCustomRole.psm1
```
But I get the following error:
```
New-AzureRmRoleDefinition : Cannot bind parameter 'InputFile'. Cannot convert value ".\MyCustomRole.psm1" to type
"Microsoft.Azure.Commands.Resources.Models.Authorization.PSRoleDefinition". Error: "Unable to find type
