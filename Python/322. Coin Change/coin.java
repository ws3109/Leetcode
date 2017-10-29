class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        final int INF = 0x7fffffff;
        for(int i = 0; i <= amount; i++)
            dp[i] = INF;
        dp[0] = 0;
        for(int coin: coins){
            for(int j = coin; j <= amount; j++){
                if(dp[j-coin] != INF)
                    dp[j] = Math.min(dp[j], dp[j-coin] + 1);
            }
        }
        return dp[amount] == INF? -1: dp[amount];
    }
}
