-- # Write your MySQL query statement below
-- SELECT patient_id, patient_name, conditions
-- FROM Patients
-- WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';



















select patient_id,patient_name,conditions from Patients where conditions like 'DIAB1%' OR conditions like '% DIAB1%'