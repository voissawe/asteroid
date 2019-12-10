---
description: This page contains all methods of AsteroidDB.
---

# Methods

There is a list below which you can find all methods of AsteroidDB. All results \(errors, replies etc.\) are in JSON response. So you need to use a JSON component in your programming language to parse the AsteroidDB's results.

{% api-method method="post" host="https://yourasteroiddb.herokuapp.com" path="/store" %}
{% api-method-summary %}
Store
{% endapi-method-summary %}

{% api-method-description %}
Store a value along with tag, or changes the value of tag to database if you are using an existing tag.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="tag" type="string" required=true %}
A unique key which used for managing the value.
{% endapi-method-parameter %}

{% api-method-parameter name="value" type="string" required=true %}
Value to store.
{% endapi-method-parameter %}

{% api-method-parameter name="pass" type="string" required=false %}
The current database password, you can leave this empty if your database is not protected with password. 
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`tag` parameter gives tag of the stored record.  
`value` parameter gives value of the stored record.
{% endapi-method-response-example-description %}

```
{    
    "action": "STORED",    
    "tag": "...",
    "value": "..."
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://yourasteroiddb.herokuapp.com" path="/get" %}
{% api-method-summary %}
Get Value
{% endapi-method-summary %}

{% api-method-description %}
Get the value from database with using tag.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="tag" type="string" required=true %}
A unique key which used for managing the value.
{% endapi-method-parameter %}

{% api-method-parameter name="pass" type="string" required=false %}
The current database password, you can leave this empty if your database is not protected with password. 
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`tag` parameter gives the tag of the record.  
`value` parameter gives the value of the record.
{% endapi-method-response-example-description %}

```
{    
    "action": "GOT",    
    "tag": "...",
    "value": "..."
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://yourasteroiddb.herokuapp.com" path="/getall" %}
{% api-method-summary %}
Get All Tags
{% endapi-method-summary %}

{% api-method-description %}
Get all tags from database. Tags are returned in JSON array.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="pass" type="string" required=false %}
The current database password, you can leave this empty if your database is not protected with password. 
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`tag` parameter gives the all tag names as a array. Password record is excluded.
{% endapi-method-response-example-description %}

```
{    
    "action": "TAGS",    
    "tag": ["...", "..."]
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://yourasteroiddb.herokuapp.com" path="/delete" %}
{% api-method-summary %}
Delete
{% endapi-method-summary %}

{% api-method-description %}
Delete a record using tag.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="tag" type="string" required=true %}
A unique key which used for managing the value.
{% endapi-method-parameter %}

{% api-method-parameter name="pass" type="string" required=false %}
The current database password, you can leave this empty if your database is not protected with password. 
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`tag` parameter gives the tag of the deleted record.
{% endapi-method-response-example-description %}

```
{    
    "action": "DELETED",    
    "tag": "..."
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully. 
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://yourasteroiddb.herokuapp.com" path="/format" %}
{% api-method-summary %}
Format
{% endapi-method-summary %}

{% api-method-description %}
Deletes every record from database, including password protection! **There is no way to recover them again!**
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="pass" type="string" required=false %}
The current database password, you can leave this empty if your database is not protected with password.
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`count` parameter gives the record count of how many records are deleted.
{% endapi-method-response-example-description %}

```
{    
    "action": "FORMATTED",    
    "count": 6
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://yourasteroiddb.herokuapp.com" path="/auth/password" %}
{% api-method-summary %}
Set / Change Password
{% endapi-method-summary %}

{% api-method-description %}
Change or set a password for database. **Setting a password will require a password in all other operations.**
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="newpass" type="string" required=true %}
Password which will replace the old one.
{% endapi-method-parameter %}

{% api-method-parameter name="oldpass" type="string" required=false %}
The current database password, you can leave this empty if your database is not protected with password.
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`action` parameter can have two values in this method. If password is changed, `action` will be `CHANGED PASSWORD`, but if password is set for the first time, it will be `SET PASSWORD`.  
  
`newpass` parameter returns the new password.
{% endapi-method-response-example-description %}

```
{    
    "action": "CHANGED PASSWORD",    
    "newpass": "******"
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://yourasteroiddb.herokuapp.com" path="/auth/unlock" %}
{% api-method-summary %}
Unlock
{% endapi-method-summary %}

{% api-method-description %}
Removes password protection by deleting password record. **Deleting the password will not require a password in all other operations anymore.**  
  
_Password protection needs to be enabled to use this method. So this method won't work with no-password databases._
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="pass" type="string" required=true %}
The current database password.
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`pass` parameter returns the password which same as in the input.
{% endapi-method-response-example-description %}

```
{    
    "action": "DELETED PASSWORD",    
    "pass": "******"
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://yourasteroiddb.herokuapp.com" path="/auth/data" %}
{% api-method-summary %}
Get Data
{% endapi-method-summary %}

{% api-method-description %}
Gives all data in the database by returning tags and values of every record. This method doesn't include password record for security.   
  
_Password protection needs to be enabled to use this method. So this method won't work with no-password databases._
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="pass" type="string" required=true %}
The current database password.
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`data` parameter returns an array which contains tag, value pairs.
{% endapi-method-response-example-description %}

```
{    
    "action": "DELETED PASSWORD",    
    "data": [
        ["tag1","value1"],
        ["tag2","value2"]
    ]
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://yourasteroiddb.herokuapp.com" path="/istrue" %}
{% api-method-summary %}
Is True
{% endapi-method-summary %}

{% api-method-description %}
Returns `true` in the result if database password is the same with the entered `pass` parameter. Otherwise, `false`.   
  
This method can be useful in applications to check the password before connecting to the database.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="pass" type="string" required=false %}
The current database password, you can leave this empty if your database is not protected with password.
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`result` parameter returns `true` if the `pass` parameter is the same with the database password, otherwise `false`.
{% endapi-method-response-example-description %}

```
{    
    "action": "IS CORRECT",    
    "result": false
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://yourasteroiddb.herokuapp.com" path="/islocked" %}
{% api-method-summary %}
Is Locked
{% endapi-method-summary %}

{% api-method-description %}
Returns `true` in the result if database is locked with password, otherwise `false`.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`result` parameter returns `true` if database has password, otherwise `false`.
{% endapi-method-response-example-description %}

```
{    
    "action": "IS LOCKED",    
    "result": false
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://yourasteroiddb.herokuapp.com" path="/count" %}
{% api-method-summary %}
Count
{% endapi-method-summary %}

{% api-method-description %}
Returns a number which tells how many records there are in the database. You can just use this method to learn record count without getting tag list or value list.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Action is executed successfully.  
  
`count` parameter returns current record count.
{% endapi-method-response-example-description %}

```
{    
    "action": "COUNT",    
    "count": 100
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
Action is not executed successfully.
{% endapi-method-response-example-description %}

```
{
    "action": "ERROR",
    "result": "(Error message)"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

