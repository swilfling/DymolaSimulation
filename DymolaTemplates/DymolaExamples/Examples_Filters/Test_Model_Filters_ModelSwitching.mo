within DymolaExamples.Examples_Filters;
model Test_Model_Filters_ModelSwitching
  parameter Real y_start=0;
  parameter Real fmi_NumberOfSteps = 1000;
  parameter Real fmi_StartTime=0;
  parameter Real fmi_StopTime=10;
  Modelica.Blocks.Sources.Pulse InputSignal(
    startTime=0.1,
    period=2,
    offset=0.1)
               annotation (Placement(transformation(extent={{-68,-20},{-48,0}})));
      Chebyshev UUT( y_start=y_start)    annotation (Placement(transformation(extent={{-22,-20},
            {-2,0}})));
equation

  connect(InputSignal.y, UUT.u1)
                                annotation (Line(points={{-47,-10},{-41.28,-10},
          {-41.28,-8.8},{-24,-8.8}},                          color={255,127,
          0}));
end Test_Model_Filters_ModelSwitching;
