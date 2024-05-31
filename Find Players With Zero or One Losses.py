
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_count = {}
        loss_count = {}
        
        for winner, loser in matches:
            if winner not in win_count:
                win_count[winner] = 0
            win_count[winner] += 1
            
            if loser not in loss_count:
                loss_count[loser] = 0
            loss_count[loser] += 1
        never_lost = []
        for player in win_count:
            if player not in loss_count:
                never_lost.append(player)       
        lost_one = []
        for player in loss_count:
            if loss_count[player] == 1:
                lost_one.append(player)
        
        return [sorted(never_lost), sorted(lost_one)]
