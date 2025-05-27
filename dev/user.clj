(ns user
  (:require
   [clj-reload.core]))

(comment

  (clj-reload.core/init
   {:dirs ["src" "dev" "test"]})

  (clj-reload.core/reload)

  :end)
