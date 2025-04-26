
Dynamic IDA Enrichment (aka. DIE)
=================================

<p align="center">
<img src="https://github.com/ynvb/DIE/blob/master/DIE/icons/logo.png" alt="DIE Logo"/>
</p>

### Original plugin

https://github.com/ynvb/DIE

### What is it?

DIE is an IDA python plugin designed to enrich IDA`s static analysis with dynamic data.
This is done using the IDA Debugger API, by placing breakpoints in key locations and saving the current system context once those breakpoints are hit.

The saved context consist of function arguments and register states, and it is saved upon each function CALL and function RETURN.

DIE takes advantage of IDA`s powerful analysis engine so that when context is taken DIE is fully aware of known function prototypes, data types, structures, unions, arrays and basically every piece of information IDA provides during static analysis.

In order to take this one step further, once context has been saved, DIE attempts to parse the individual data types based on an integrated (and extensible!) value parser framework.

So for example, if the current context has a function argument with type 'CHAR *' DIE will dereference its address and show a human readable ASCII string as value.

If the current context holds a argument with unknown value, DIE will not give up and attempt to guess the value using all relevant parsers.

This parser framework is the real power behind DIE, parser plugins can parse anything from BOOL values to image files to injected code.

The resault is a dynamic databse that holds parsed runtime arguments, which are avilable to the user during static analysis.

