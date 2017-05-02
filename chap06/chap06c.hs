import System.Environment
import Data.Char (digitToInt)

type Expression = [Term]
type Term = [Factor] 
type Factor = [Digit] 
type Digit = Int

good c (_, f, t, e)  = (f * t + e ==c)
ok c (_, f, t, e)    = (f * t + e <= c)

modify x (k, f, t, e) = [(10 * k, k * x + f, t, e), (10, x, f * t, e), (10, x, 1, f * t + e)]

solutions :: Int -> [Digit] -> [Expression]
solutions c = map fst . filter (good c . snd) . foldr (expand c) []

expand c x [] = [([[[x]]], (10, x, 1, 0))]
expand c x evs = concat (map (filter (ok c . snd) . glue x) evs)

glue x ((xs : xss) : xsss, (k, f, t, e)) =
    [(((x : xs) : xss) : xsss, (10*k, k*x + f, t, e)),
    (([x] : xs : xss) : xsss, (10, x, f * t, e)),
    ([[x]] : (xs : xss) : xsss, (10, x, 1, f * t + e))]

main = do
    (sumStr:digitsStr:_) <- getArgs
    let digits = map digitToInt digitsStr
    let sum = read sumStr :: Int
    putStrLn $ "Number of solutions found: " ++ (show $ length $ solutions sum digits)

