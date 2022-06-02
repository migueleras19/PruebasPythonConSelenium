/**
 * modularjs: A modular javascript system
 * 
 * How to use:
 * 
 * 1. Add to head:
 *      <script type="text/javascript"
 *          src="include.js?somepackage.SomeModule1,somepackage.SomeModule2">
 *      </script>
 * 
 * 2. And anywhere in your js files:
 *      include("somepackage.SomeOtherModule");
 * 
 * Modules are loaded from [package]/[subpackage]/[ModuleName].js files.
 * 
 * See the README file to learn how to compile your modules into a single
 * compressed file.
 * 
 * http://modularjs.googlecode.com
 */

var MODULARJS_SET_GLOBAL_VAR_NAME = "__modularjs_global_test__";
var MODULARJS_SET_GLOBAL_VAR = "var " + MODULARJS_SET_GLOBAL_VAR_NAME +
                               " = true;";

var modularjs = {

    basePath: null,

    loaded: {},

    loading: {},

    /**
     * Inits the modularjs system.
     */
    init: function() {
        /*globals ActiveXObject */

        if (typeof XMLHttpRequest != "undefined") {
            modularjs.xhr = new XMLHttpRequest();
        } else if (typeof ActiveXObject != "undefined") {
            modularjs.xhr = new ActiveXObject("Microsoft.XMLHTTP");
        } else {
            throw new Error("XMLHttpRequest not supported");
        }

        modularjs.head = document.getElementsByTagName("head")[0];
        var scripts = modularjs.head.getElementsByTagName("script");

        modularjs.setEvalFunction();

        for ( var i = 0; i < scripts.length; i++) {
            var src = scripts[i].src;
            if (src && src.match(/.*include\.js.*/)) {
                var parts = src.split(/\?/);
                modularjs.basePath = parts[0].replace(/include\.js.*/, '');
                if (parts.length > 1) {
                    parts = parts[1].split(",");
                    for ( var j = 0; j < parts.length; j++) {
                        modularjs.include(parts[j]);
                    }
                }
            }
        }
    },

    setGlobal: function(evalFunction) {
        if (!!window[MODULARJS_SET_GLOBAL_VAR_NAME]) {
            try {
                delete window[MODULARJS_SET_GLOBAL_VAR_NAME];
            } catch (e) {
                window[MODULARJS_SET_GLOBAL_VAR_NAME] = undefined;
            }
        }
        evalFunction(MODULARJS_SET_GLOBAL_VAR);
        if (!!window[MODULARJS_SET_GLOBAL_VAR_NAME]) {
            modularjs.eval = evalFunction;
            return true;
        } else {
            return false;
        }
    },

    execScript: function(contents) {
        if (window.execScript) {
            window.execScript(contents);
        }
    },

    withWindowEval: function(contents) {
        with (window) {
            window.eval(contents);
        }
    },

    insertScript: function(contents) {
        var script = document.createElement("script");
        script.type = "text/javascript";
        script.text = contents;
        modularjs.head.appendChild(script);
        modularjs.head.removeChild(script);
    },

    /**
     * Sets the best function to be used.
     */
    setEvalFunction: function() {
        if (modularjs.setGlobal(modularjs.execScript)) {
            return;
        }

        if (modularjs.setGlobal(modularjs.withWindowEval)) {
            return;
        }

        if (modularjs.setGlobal(modularjs.insertScript)) {
            return;
        }

        throw new Error("Cannot determine a good eval function");
    },

    /**
     * Includes a module. Only absolute includes.
     * It's aliased to the global function 'include'.
     *
     * @param module {string} The module name (dot separated)
     * @returns true if module was included correctly
     */
    include: function(module) {
        if (!module) {
            throw new Error("No module name defined");
        }

        if (modularjs.loaded[module]) {
            return true;
        }

        if (modularjs.loading[module]) {
            throw new Error("Possible recursive import: " + module);
        }

        modularjs.loading[module] = true;

        var contents = modularjs.getContents(module);

        try {
            modularjs.eval(contents);
            modularjs.loaded[module] = true;
        } catch (e) {
            if (typeof console != "undefined") {
                console.error("Error importing module: " + module, e);
            }
            throw e;
        }

        modularjs.loading[module] = false;

        return !!modularjs.loaded[module];
    },

    includeCSS: function(module) {
        var filename = "css/" + module.replace(/\./g, "/") + ".css";
        var link = document.createElement("link");

        link.setAttribute("type", "text/css");
        link.setAttribute("rel", "stylesheet");
        link.setAttribute("href", filename);

        document.getElementsByTagName("head")[0].appendChild(link);
    },
    
    /**
     * Returns the best filename that corresponds to a module.
     *
     * @param module {string} The module name
     * @returns The module filename
     */
    getContents: function(module) {
        var contents = null;
        var filename = null;
        this.ie = Prototype.Browser.IE;

        filename = module.replace(/\./g, "/") + ".js";
        contents = modularjs.getFileContents(filename);

        if (contents) {
            if (this.ie) {
                return contents;
            }

            return contents + "\r\n//@ sourceURL=" + filename;
        }

        throw new Error("Module " + module + " not found.");
    },

    /**
     * Checks for file existence
     *
     * @param filename {string} With the filename
     * @returns The module filename
     */
    getFileContents: function(filename) {
        try {
            // FIXME: Cambio temporal para Chrome 48. Se evita que use la cache, lo que causa que
            // responseText de AJAX sea "".
            modularjs.xhr.open("get", modularjs.basePath + filename + '?_=' + new Date().getTime(), false);
            modularjs.xhr.send(null);

            if (modularjs.xhr.status == 0 || modularjs.xhr.status == 200) {
                return modularjs.xhr.responseText;
            }
        } catch (e) {
        }

        return "";
    }

};

var include = modularjs.include;
includeCSS = modularjs.includeCSS;

if (typeof __build__ == "undefined") {
    modularjs.init();
}

