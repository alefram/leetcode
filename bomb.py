def bomb_iteraction(num_claims, bcoin_invested, claim_return, claim_porcentage):
    claim = 40
    re_investment = 0
    ganancias = 20
    for i in range(num_claims):
        re_investment = bcoin_invested + claim * claim_return
        bcoin_invested = re_investment
        claim = bcoin_invested  * claim_porcentage
        ganancias = claim - claim * claim_return
        roi = (claim / bcoin_invested) * 100

        print('reclamo',i+1)
        print('--------------------')
        print("bc invertido:",re_investment,"bc reclamados:",claim)
        print('ganancias:', ganancias)
        print('ROI:',roi)
        print('--------------------')


if __name__ == '__main__':
    bomb_iteraction(10,70,1,0.4)
