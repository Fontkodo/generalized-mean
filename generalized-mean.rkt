#lang racket/base

(require (only-in racket/contract contract-out -> listof)
         (only-in racket/function curry))

(provide
 (contract-out
  [ generalized-mean (-> real? (listof positive?) real?)]
  [ geometric-mean   (-> (listof positive?) real? )]
  [ harmonic-mean    (-> (listof positive?) real? )]
  [ quadratic-mean   (-> (listof positive?) real? )]))

(define (avg nums)
  (/ (apply + nums)
     (length nums)))

(define (generalized-mean exponent nums)
  (if (zero? exponent)
      (expt (apply * nums)
            (/ (length nums)))
      (expt (avg (for/list ((n (in-list nums)))
                   (expt n exponent)))
            (/ exponent))))

(define geometric-mean (curry generalized-mean  0))
(define harmonic-mean  (curry generalized-mean -1))
(define quadratic-mean (curry generalized-mean  2))



;==============================================

(module+ main
  (define stuff '(1 10 8 3 5 6 10 9 8))
  (for ((exponent (in-range -5 5 .5)))
    (printf "~a\t~a\n" exponent (generalized-mean exponent stuff))))

;==============================================

(module+ test
  (require rackunit)
  
  (define stuff '(1 10 8 3 5 6 10 9 8))
  
  (check-equal?
   (avg stuff)
   (generalized-mean 1 stuff))

  (check-equal?
   (generalized-mean 0 stuff)
   (geometric-mean stuff))

  (check-equal?
   (generalized-mean -1 stuff)
   (harmonic-mean stuff))

  (check-equal?
   (generalized-mean 2 stuff)
   (quadratic-mean stuff))
  
  (check-true
   (< (generalized-mean 1 stuff)
      (generalized-mean 2 stuff)
      (generalized-mean 3 stuff))))
