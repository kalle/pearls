import System.Environment
import Data.Char (digitToInt)

type Expression = [Term]
type Term = [Factor] 
type Factor = [Digit] 
type Digit = Int

valExpr :: Expression -> Int 
valExpr = sum . map valTerm

valTerm :: Term -> Int
valTerm = product . map valFact 

valFact :: Factor -> Int
valFact = foldl1 (\n d -> 10 * n + d)

expressions :: [Digit] -> [Expression] 
expressions = concatMap partitions . partitions

partitions [] = [[]]
partitions (x:xs) = [[x]:p | p <- partitions xs]
                 ++ [(x:ys):yss | (ys:yss) <- partitions xs]

good :: Int -> Int -> Bool
good c v = c == v

goodOnes :: Digit -> [Digit] -> [Expression]
goodOnes c = filter (good c . valExpr) . expressions

main = do
    (sumStr:digitsStr:_) <- getArgs
    let digits = map digitToInt digitsStr
    let sum = read sumStr :: Int
    putStrLn $ "Number of solutions found: " ++ (show $ length $ goodOnes sum digits)

