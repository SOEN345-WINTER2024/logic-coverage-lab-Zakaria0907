import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class CheckItTest {

    private final PrintStream originalSystemOut = System.out;
    private final ByteArrayOutputStream testOutputContent = new ByteArrayOutputStream();

    @Before
    public void setUpOutput() {
        System.setOut(new PrintStream(testOutputContent));
    }

    @After
    public void restoreSystemOutput() {
        System.setOut(originalSystemOut);
        testOutputContent.reset();
    }

    // CLAUSE COVERAGE
    @Test
    public void whenAllClausesAreTrue_thenOutputShouldBeTrue() {
        CheckIt.checkIt(true, true, true);
        assertEquals("P is true", testOutputContent.toString().trim());
    }

    @Test
    public void whenAllClausesAreFalse_thenOutputShouldBeFalse() {
        CheckIt.checkIt(false, false, false);
        assertEquals("P isn't true", testOutputContent.toString().trim());
    }

    // PREDICATE COVERAGE
    @Test
    public void whenPredicateIsTrue_thenOutputShouldBeTrue() {
        CheckIt.checkIt(true, false, true);
        assertEquals("P is true", testOutputContent.toString().trim());
    }

    @Test
    public void whenPredicateIsFalse_thenOutputShouldBeFalse() {
        CheckIt.checkIt(false, true, false);
        assertEquals("P isn't true", testOutputContent.toString().trim());
    }

    // CACC COVERAGE
    @Test
    public void whenCACCTrue_thenOutputShouldBeTrue() {
        CheckIt.checkIt(true, true, false);
        assertEquals("P is true", testOutputContent.toString().trim());
    }

    @Test
    public void whenCACCFails_thenOutputShouldBeFalse() {
        CheckIt.checkIt(false, true, false);
        assertEquals("P isn't true", testOutputContent.toString().trim());
    }

    // RACC COVERAGE
    @Test
    public void whenRACCTrue_thenOutputShouldBeTrue() {
        CheckIt.checkIt(true, false, true);
        assertEquals("P is true", testOutputContent.toString().trim());
    }

    @Test
    public void whenRACCFails_thenOutputShouldBeFalse() {
        CheckIt.checkIt(false, false, true);
        assertEquals("P isn't true", testOutputContent.toString().trim());
    }
}
