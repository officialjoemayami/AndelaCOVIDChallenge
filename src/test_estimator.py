from src.estimator import app
import unittest
import json

info = {
"region": {
"name": "Africa",
"avgAge": 19.7,
"avgDailyIncomeInUSD": 4,
"avgDailyIncomePopulation": 0.73
},
"periodType": "days",
"timeToElapse": 38,
"reportedCases": 2747,
"population": 92931687,
"totalHospitalBeds": 678874
}

class EstimatorTest(unittest.TestCase):
  # check logs
  def test_logs(self):
    tester = app.test_client(self)
    res = tester.get('/api/v1/on-covid-19/logs')
    status = res.status_code
    self.assertEqual(status, 200)
  
  # check default
  def test_default(self):
    tester = app.test_client(self)
    res = tester.post('/api/v1/on-covid-19', data=json.dumps(info), headers={'Content-Type': 'application/json'})
    status = res.status_code
    self.assertEqual(status, 200)

  # check json
  def test_json(self):
    tester = app.test_client(self)
    res = tester.post('/api/v1/on-covid-19/json', data=json.dumps(info), headers={'Content-Type': 'application/json'})
    status = res.status_code
    self.assertEqual(status, 200)

  # check xml
  def test_xml(self):
    tester = app.test_client(self)
    res = tester.post('/api/v1/on-covid-19/xml', data=json.dumps(info), headers={'Content-Type': 'application/json'})
    status = res.status_code
    self.assertEqual(status, 200)


if __name__ == "__main__":
    unittest.main()