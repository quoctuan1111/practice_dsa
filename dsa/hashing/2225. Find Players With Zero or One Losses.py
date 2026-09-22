class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        count = defaultdict(int)
        for winner, loser in matches:
            count[winner] 
            count[loser] += 1

        no_losses = []
        one_loss = []

        for player, loss_count in count.items():
            if loss_count == 0:
                no_losses.append(player)
            elif loss_count == 1:
                one_loss.append(player)
        return [sorted(no_losses), sorted(one_loss)]

        

