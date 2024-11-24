import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail; // Used for handling exceptions in JUnit 4
import org.junit.Test;

public class JavaExampleTest {

	// Test for Grade A
	@Test
	public void testCalculateGrade_A() {
		int[] marks = { 85, 90, 80, 95, 85, 88 };
		assertEquals("A", JavaExample.calculateGrade(marks)); // Expected grade: A
	}

	// Test for Grade B
	@Test
	public void testCalculateGrade_B() {
		int[] marks = { 65, 60, 70, 68, 62, 61 };
		assertEquals("B", JavaExample.calculateGrade(marks)); // Expected grade: B
	}

	// Test for Grade C
	@Test
	public void testCalculateGrade_C() {
		int[] marks = { 40, 45, 50, 42, 44, 46 };
		assertEquals("C", JavaExample.calculateGrade(marks)); // Expected grade: C
	}

	// Test for Grade D
	@Test
	public void testCalculateGrade_D() {
		int[] marks = { 30, 20, 25, 35, 28, 32 };
		assertEquals("D", JavaExample.calculateGrade(marks)); // Expected grade: D
	}

	// Edge case: Average exactly 80 (should be Grade A)
	@Test
	public void testCalculateGrade_Exact80() {
		int[] marks = { 80, 80, 80, 80, 80, 80 };
		assertEquals("A", JavaExample.calculateGrade(marks)); // Expected grade: A
	}

	// Edge case: Average exactly 60 (should be Grade B)
	@Test
	public void testCalculateGrade_Exact60() {
		int[] marks = { 60, 60, 60, 60, 60, 60 };
		assertEquals("B", JavaExample.calculateGrade(marks)); // Expected grade: B
	}

	// Edge case: Average exactly 40 (should be Grade C)
	@Test
	public void testCalculateGrade_Exact40() {
		int[] marks = { 40, 40, 40, 40, 40, 40 };
		assertEquals("C", JavaExample.calculateGrade(marks)); // Expected grade: C
	}

	// Test for invalid input: Negative marks
	@Test
	public void testCalculateGrade_InvalidInputNegative() {
		int[] marks = { 85, -10, 80, 95, 85, 88 }; // Contains a negative mark
		try {
			JavaExample.calculateGrade(marks);
		} catch (IllegalArgumentException e) {
			assertEquals("Marks must be between 0 and 100.", e.getMessage()); // Check error message
			return;
		}
		fail("Expected IllegalArgumentException was not thrown."); // Test fails if exception is not thrown
	}

	// Test for invalid input: Marks above 100
	@Test
	public void testCalculateGrade_InvalidInputAbove100() {
		int[] marks = { 85, 110, 80, 95, 85, 88 }; // Contains a mark above 100
		try {
			JavaExample.calculateGrade(marks);
		} catch (IllegalArgumentException e) {
			assertEquals("Marks must be between 0 and 100.", e.getMessage()); // Check error message
			return;
		}
		fail("Expected IllegalArgumentException was not thrown."); // Test fails if exception is not thrown
	}
}
