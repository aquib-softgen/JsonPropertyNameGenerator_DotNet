# JPN PARSER TOOL
Generates JsonPropertyNames() with snake_case values for each field in a C# class

## USAGE
Clone the repo and add the directory path to Environment variable and refresh the termial to reload PATH.
```
git clone https://github.com/aquib-softgen/JsonPropertyNameGenerator_DotNet.git
```

Here is how you will modify a file with properties inplace by creating a temporary file while 
performing the operation

```
cat YourDotNetFile.cs | jpn_parser > temp && cat temp > YourDotNetFile.cs && rm temp
```