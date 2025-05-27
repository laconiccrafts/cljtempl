(ns cljtempl.core
  (:require
   clojure+.error
   clojure+.hashp
   clojure+.print
   clojure+.test))

(clojure+.hashp/install!)
(clojure+.print/install-printers!)
(clojure+.print/install-readers!)
(clojure+.error/install! {:reverse? true})
(clojure+.test/install!)