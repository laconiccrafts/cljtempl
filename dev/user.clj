(ns user
  (:require
   [clj-reload.core]))

(clj-reload.core/init
 {:dirs ["src" "dev" "test"]})

(comment
  (clj-reload.core/reload)

  :end)