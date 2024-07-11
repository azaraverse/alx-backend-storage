-- A SQL script that creates a stored procedure ComputeAverageScoreForUser() that computes and stores the average score for a student.

DELIMITER $$
-- Create stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- declare a variable to hold the computed average score
    DECLARE average_score FLOAT DEFAULT 0;

    -- Select scores from the corrections table and compute the average score
    SELECT AVG(score) INTO average_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Update the users table with the computed average score
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END $$
DELIMITER ;
