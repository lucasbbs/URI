class Experiment:
  def __init__(self, amount, kind):
    self.amount = amount
    self.kind = kind
N = int(input())
experiments = []
for i in range(0,N):
  amountInput, kindInput = input().split()
  experiments.append(Experiment(int(amountInput), kindInput))
print(f'Total: {sum(experiment.amount for experiment in experiments)} cobaias')
print(f'Total de coelhos: {sum(experiment.amount for experiment in experiments if experiment.kind == "C")}')
print(f'Total de ratos: {sum(experiment.amount for experiment in experiments if experiment.kind == "R")}')
print(f'Total de sapos: {sum(experiment.amount for experiment in experiments if experiment.kind == "S")}')
print(f'Percentual de coelhos: {sum(experiment.amount for experiment in experiments if experiment.kind == "C")/sum(experiment.amount for experiment in experiments)*100:.2f} %')
print(f'Percentual de ratos: {sum(experiment.amount for experiment in experiments if experiment.kind == "R")/sum(experiment.amount for experiment in experiments)*100:.2f} %')
print(f'Percentual de sapos: {sum(experiment.amount for experiment in experiments if experiment.kind == "S")/sum(experiment.amount for experiment in experiments)*100:.2f} %')