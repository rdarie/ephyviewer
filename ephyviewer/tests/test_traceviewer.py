import numpy as np
import ephyviewer
from  ephyviewer.tests.testing_tools import make_fake_signals, make_fake_signals_with_scatter

import neo
import quantities as pq


def test_traceviewer():
    source = make_fake_signals()


    app = ephyviewer.mkQApp()
    view = ephyviewer.TraceViewer(source=source, name='trace')
    #~ view.refresh()


    win = ephyviewer.MainViewer(debug=True, show_auto_scale=True)
    win.add_view(view)
    win.show()

    app.exec_()


def test_traceviewer_with_scatter():
    source = make_fake_signals_with_scatter()

    #~ exit()

    app = ephyviewer.mkQApp()
    view = ephyviewer.TraceViewer(source=source, name='trace_with_scatter')
    #~ view.refresh()


    win = ephyviewer.MainViewer(debug=True, show_auto_scale=True)
    win.add_view(view)
    win.show()

    app.exec_()



def test_traceviewer_cls_method_numpy():
    sigs = np.random.rand(100000,16)
    sample_rate = 1000.
    t_start = 0.

    app = ephyviewer.mkQApp()
    view = ephyviewer.TraceViewer.from_numpy(sigs, sample_rate, t_start, 'sigs')

    win = ephyviewer.MainViewer(debug=True, show_auto_scale=True)
    win.add_view(view)
    win.show()
    app.exec_()

def test_traceviewer_cls_method_neo():
    sigs = np.random.rand(100000,16)
    sample_rate = 1000.
    t_start = 0.

    neo_anasig = neo.AnalogSignal(sigs*pq.mV, sampling_rate=sample_rate*pq.Hz, t_start=0*pq.s, copy=True)
    print(neo_anasig)


    app = ephyviewer.mkQApp()

    view = ephyviewer.TraceViewer.from_neo_analogsignal(neo_anasig, 'sigs')
    win = ephyviewer.MainViewer(debug=True, show_auto_scale=True)
    win.add_view(view)
    win.show()
    app.exec_()



if __name__=='__main__':
    #~ test_traceviewer()
    #~ test_traceviewer_with_scatter()
    #~ test_traceviewer_cls_method_numpy()
    test_traceviewer_cls_method_neo()
